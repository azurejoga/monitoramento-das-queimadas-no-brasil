# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec720522-beb9-3515-a307-7854bb1a3d94 | -17.58987 | -57.4763 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1784ff7f-b763-36ef-a3a2-afd187dd1c87 | -17.57252 | -57.45272 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 35f190e8-2c6b-34e8-9cdd-c2d79b341f35 | -17.56542 | -57.5783 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 2f322024-e8fd-36ab-9db4-1e31f157d34f | -17.59517 | -57.57146 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| a1e7bad2-9f5f-3279-954e-dca70651b6e0 | -15.91979 | -59.27432 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| a10af60e-785b-36db-ab27-90a39bf22852 | -15.90067 | -59.27014 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| e188caae-5aea-3947-ac75-12c93af2e152 | -15.96801 | -57.28014 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa8af490-5ce4-38e9-95dd-45a3cab64f8d | -15.66833 | -59.73547 | 2024-11-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e24dd2a8-e985-34b4-a0c4-dd741b56f662 | -17.23475 | -57.18777 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ec744740-efbd-3d91-a5da-94903e5bc71c | -17.58613 | -57.56156 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8592c75b-4e24-3a02-a089-fc78e6cdab01 | -9.92208 | -59.91117 | 2024-11-16 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9301db1c-c708-398d-b8ed-3c74fa4c784e | -17.58275 | -57.5815 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.2 |
| 4e30b09b-f862-374c-abf3-8993aa768b50 | -17.55001 | -57.52207 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 3dfc121d-9d99-396f-b857-4de2c22f2267 | -17.36455 | -57.43651 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 3547c9d0-3293-3b22-b569-d57cd2f0a81a | -17.64273 | -57.54332 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 2204ca3c-9c20-3aba-baa5-b41ad108d01e | -9.24984 | -63.62621 | 2024-11-16 04:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7f36038-6a80-3274-9ec9-735ddaf04878 | -16.93971 | -57.62654 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 11bdd0d6-27ff-36c7-ae7e-56f2cc8ad713 | -17.80789 | -57.55923 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 37beaabc-efa0-397f-b9d9-b73e325a1875 | -16.9467 | -57.62783 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 63f57043-a96a-3b81-86b5-8d34bd221076 | -17.55075 | -57.5386 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 3e832099-a04d-3585-86c5-442bada56d55 | -17.82834 | -54.5452 | 2024-11-16 04:53:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b3beac67-b17c-3b80-bd35-85cde63b9586 | -22.27052 | -56.10455 | 2024-11-16 04:53:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1981fd86-b317-3822-a98b-d15496f7b6fb | -16.09992 | -60.10201 | 2024-11-16 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7cfa9207-3e06-3e14-831f-b0d23d2467c4 | -17.29873 | -57.30723 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 99a8abf9-ef30-313d-a8fd-94e7ed5a0472 | -17.66551 | -57.54585 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 6f0ba802-dc25-3bbf-91e5-03c9628fdf19 | -17.57009 | -57.52988 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1e319e89-4003-36bc-b74c-66cbde164e32 | -17.57808 | -57.46188 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ff06ee95-6bce-3ff4-ae29-111ef28fc76a | -16.922 | -57.54014 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4fe3fe38-025a-3b4f-bc19-5a4beb09f970 | -17.82502 | -54.54464 | 2024-11-16 04:53:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5d74faa1-560b-3fc2-963f-dac5652ee5dc | -17.62769 | -57.56927 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.2 |
| 96784f18-2e74-3376-9f6c-012a7e07da56 | -17.55768 | -57.53988 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b93f27c4-7d79-34fd-b2aa-5c2ae7708b6a | -17.56038 | -57.524 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2e47bda6-781a-39df-b567-4ed627d99654 | -17.5705 | -57.46457 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 41ca5e98-84a0-375a-9054-e21f43b3a000 | -17.61651 | -57.55077 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 783055df-009b-399c-864b-3317c5c5f289 | -17.56535 | -57.55772 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| de55ad95-aab5-33bb-94f2-07b0c084bb34 | -17.56738 | -57.54578 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f07d6b07-18c0-3551-9e4c-22f8dd9f66fc | -15.97081 | -57.28478 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a452912a-44fa-34aa-917a-3d41e55fb890 | -17.63527 | -57.46022 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6a300f64-0839-3e08-ac69-8aa2a5b512a0 | -17.67589 | -57.54776 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5f4744d2-3965-3b35-873d-9577d15f5839 | -17.56392 | -57.54514 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 2c244a0e-4065-3afe-898f-2821f908e821 | -17.66663 | -57.4766 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7ae78d6f-0a0c-3b62-9c3e-d8599a508857 | -17.5814 | -57.58947 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| a3953709-7b20-3718-9773-ec6d0c703d76 | -17.22724 | -57.1904 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c76d5d25-d9a3-39a0-b7fc-df1d74b2048d | -17.55489 | -57.53527 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| fbe34679-361e-3362-809a-a4f06bc4616a | -17.55557 | -57.5313 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| da96d963-49f4-3f30-ab80-6d194e1c6c9f | -17.56933 | -57.51336 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| b9b01ee3-1bbc-38f4-86e5-68bf614e38f6 | -22.05381 | -56.01358 | 2024-11-16 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0faed387-51dc-38f5-a2d3-493ef4cc0440 | -17.36042 | -57.43983 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 4881be70-d4fd-3c0b-aaa6-2f4e3f937be9 | -17.5753 | -57.4573 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 00ead029-7e43-3222-9448-5e8c4c298d2f | -13.48113 | -60.36221 | 2024-11-16 04:53:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f39847d5-7e12-3dae-908f-4f811f0edcb1 | -16.21352 | -59.14872 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7d01e8c6-f8c9-3989-9959-c389e4239d08 | -17.55693 | -57.52335 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 7648cb82-3187-3eb4-893a-c1d88d1c6b53 | -17.55211 | -57.53065 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 3ff44be6-e774-3449-80a0-546e2d22eaab | -17.56957 | -57.57494 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| cd37d7c3-8e92-3851-9959-5db84381b2d0 | -17.62556 | -57.56065 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 69fa53ab-ae47-372a-91ad-f0c5d227188a | -17.56264 | -57.57367 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 43e6775b-7f6c-3c13-b95e-0d0dfad01ad5 | -17.697 | -57.48627 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 14abc9db-4c73-3018-b753-d8dec68c9430 | -17.24854 | -57.45662 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2353c92f-efee-3554-854a-629f11b59bf3 | -17.54865 | -57.53002 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 25b41c62-577d-3c8b-aa1e-91a301850d7a | -17.23884 | -57.45076 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 223f8a9f-3f42-324c-9355-77f5024f9638 | -17.09403 | -57.484 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7eaf5510-0a18-3c19-8fe0-696182022c44 | -17.29807 | -57.31115 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4d13e0dd-c634-3bde-9a0d-1e8caaa38bcc | -22.2711 | -56.10083 | 2024-11-16 04:53:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 461a752e-406b-3d1e-838a-8f824b66679d | -17.65446 | -57.5479 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.9 |
| f909959c-99ea-3f1d-bd43-480a0e75170e | -16.9432 | -57.62719 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| a360b000-8e6c-3a88-a829-5c38ebe37a70 | -17.67243 | -57.54713 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 42213b51-7423-3524-998f-08b8dbb5261e | -17.62623 | -57.55667 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 3f0abb0b-e203-3b89-a247-c54537bb2f74 | -17.64007 | -57.55924 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 5c19f109-9870-36e0-abe5-581e2549b196 | -15.91298 | -59.26791 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2ad4d619-8fda-3303-96a4-0314fb94a088 | -17.68491 | -57.55763 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 2acac98c-c889-3b9e-a611-a2b4ef1af153 | -17.63927 | -57.54268 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0d38bbf9-eb02-3b0f-9e95-a3a59237121f | -17.63382 | -57.55397 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 85c09e40-1fff-31cb-bf27-a7778079b80f | -17.23816 | -57.45472 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 66a30427-41f1-3829-bfc2-361f861c6a4c | -17.24441 | -57.45996 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3c733f63-284c-3cfd-8f1f-6fa1347fc053 | -17.5646 | -57.54116 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| db0c4c7d-b486-327f-bd6d-1b92f0963a7e | -17.61997 | -57.55141 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| ec79babc-6279-3de6-b0d9-90c60d380d42 | -17.62076 | -57.56798 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 1f6b799a-d810-3e60-a338-854cd5d476f7 | -17.56814 | -57.56234 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| bca8ea78-13b5-313a-a727-3b7e3fd46dce | -17.59171 | -57.57082 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 78d47563-dafa-36af-a04f-bf358008b1bf | -15.1593 | -59.7211 | 2024-11-16 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73d90451-2ea6-324c-be17-79677726a98e | -17.57597 | -57.45335 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9a2fcc34-4cdb-30ad-beeb-2da5722c2839 | -17.69125 | -57.58343 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| c56474da-6eb0-3181-b7f8-ad66d6d9482b | -17.62489 | -57.56464 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.2 |
| d6bb61a2-9491-31c3-84b1-78fe1c7db59a | -15.97429 | -57.28543 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40c49d34-6e96-3ed2-9402-7c23a8e33b32 | -16.92269 | -57.53612 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 056b6357-3968-36b5-a0a5-0583367abf26 | -17.63661 | -57.5586 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 80a49bac-86d9-3593-81a0-c4cb07148ae6 | -14.54248 | -59.96169 | 2024-11-16 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10931089-dbef-3afa-8708-b1b4d49740bc | -17.58575 | -57.47962 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 2662233b-5188-3c88-875f-a05cbaacf37d | -15.90831 | -59.27185 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 79d0aa11-5c4c-3e8c-b545-82f3b1e012db | -17.23124 | -57.45345 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 897adec0-511f-3692-9619-dccbc6cf0e44 | -17.63728 | -57.55462 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 6fdcce10-ca66-3d4b-ba9a-77bfce136633 | -15.889 | -59.26884 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 872184ad-7b76-3b1d-be48-04ad923e049f | -17.24162 | -57.45535 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ba4e39f8-9b89-3f35-89d0-c63802328812 | -16.01652 | -59.36658 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 788c3d75-845d-3978-b13e-d7a78d42f26e | -10.02851 | -64.22701 | 2024-11-16 04:53:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d38c9139-cff1-389b-93cb-cd47d20a0291 | -17.56974 | -57.44814 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 75ebd82a-d646-3108-adaf-ad4a5f0b8400 | -17.55625 | -57.52732 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 3ae09028-35c0-3013-8309-099ffb74b208 | -17.69116 | -57.56289 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 90e7d662-ce74-3881-bbbf-bb3f7bba8ae4 | -17.58997 | -57.49673 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| d03ed2e0-9ebc-3959-b229-f352ee485c1d | -17.65514 | -57.54393 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.9 |


[Clique aqui para ver as próximas entradas](README53.md)
