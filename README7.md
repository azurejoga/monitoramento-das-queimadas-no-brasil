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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9ead130-881b-30f2-beb7-ac79d5f4fb44 | -4.47 | -44.9392 | 2025-10-13 03:30:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 175.9 |
| 5cc08d15-ec78-3943-a8f4-187a2d54ecc6 | -8.4655 | -46.1359 | 2025-10-13 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 37fcc23e-e82a-3132-9381-f11e8a0061e3 | -15.037 | -46.6501 | 2025-10-13 03:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 4ebe6814-11ce-3fd6-b6c4-598676a3b246 | -4.4888 | -44.9155 | 2025-10-13 03:30:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| f9188828-3443-3bc5-a57f-9010398e53f5 | -4.4886 | -44.9382 | 2025-10-13 03:30:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 212.0 |
| 45b8c23b-4841-386a-9f64-31031229ffb1 | -4.4701 | -44.9165 | 2025-10-13 03:30:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 53.3 |
| bc46e9fd-7f66-3df8-936a-6f5126b7fdab | -2.5423 | -47.811 | 2025-10-13 03:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| babb41f1-820d-3b84-a72b-903aedf07204 | -8.4469 | -46.1153 | 2025-10-13 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| f40fdca1-8907-36e3-ba62-090e12996664 | -7.5052 | -44.6192 | 2025-10-13 03:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 0e60d11d-64c7-318a-bf93-a07c3df07d71 | -2.5238 | -47.8115 | 2025-10-13 03:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 0f82c912-2f0e-3047-aafb-8b279f5ea874 | -7.4863 | -44.621 | 2025-10-13 03:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 4bbe89f2-5b71-381e-893a-ced0ee4aeb05 | -9.8228 | -62.1979 | 2025-10-13 03:40:00 | GOES-19 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 198b7425-5cac-3fc1-a97d-ea5ad1f86245 | -8.4658 | -46.1134 | 2025-10-13 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| f94acfb0-c759-3b11-82ef-c2cf9f1d5d42 | -8.4655 | -46.1359 | 2025-10-13 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 48bd2bac-2479-337a-95dd-b20860c0b970 | -15.057 | -46.6236 | 2025-10-13 03:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 0212dba0-f85d-34af-884b-8516420b17de | -7.4861 | -44.6439 | 2025-10-13 03:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.6 |
| dbcd5504-2caa-3a0c-a505-dfc4ab29e4af | -4.4886 | -44.9382 | 2025-10-13 03:40:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 10f7421b-10ba-37a1-8bb2-d129794f1e16 | -15.0565 | -46.6466 | 2025-10-13 03:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 4abfcceb-2ba5-3b35-a7da-f5908a344f20 | -4.47 | -44.9392 | 2025-10-13 03:40:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 5ed5a270-0561-38e2-824d-4a5c2237d8b1 | -4.6696 | -43.1326 | 2025-10-13 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 058034e6-71f0-3c14-a53f-b43e0d097424 | -17.338 | -53.8135 | 2025-10-13 03:40:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 49ecb137-4243-3678-b611-50fdc6c66288 | -8.4467 | -46.1378 | 2025-10-13 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 82198b4a-53f7-3a62-8af3-6462c251d696 | -15.0375 | -46.6271 | 2025-10-13 03:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| cc0eea98-23d4-3c2f-83a5-4b156148d4fd | -8.4467 | -46.1378 | 2025-10-13 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 47d88237-2f5f-3082-a071-27e64be87888 | -9.8228 | -62.1979 | 2025-10-13 03:50:00 | GOES-19 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 3adb675b-45e2-3c0b-a5c2-8c0bdcdd41c8 | -8.4469 | -46.1153 | 2025-10-13 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 8b842d11-ce63-3a4f-b362-7a66718bba7a | -4.47 | -44.9392 | 2025-10-13 03:50:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 54.5 |
| bb391813-4db8-3cd9-a513-f1e806f83a6b | -8.4655 | -46.1359 | 2025-10-13 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 77210cf3-ef9a-3948-974a-dc818b26d7a6 | -8.4658 | -46.1134 | 2025-10-13 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| bd5f2b13-0150-344e-a1bb-6770d884dfea | -7.4863 | -44.621 | 2025-10-13 03:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 44c125b2-b6b3-3692-8bfa-7ab5bf751d58 | -7.5052 | -44.6192 | 2025-10-13 03:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 68c97706-1811-3368-8df6-779598432a8f | -2.5238 | -47.8115 | 2025-10-13 03:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| b7d27ca6-4d27-330f-95d1-520368cdfc93 | -17.338 | -53.8135 | 2025-10-13 03:50:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 68399a00-c96e-3614-84d2-cb63520a7eb0 | -4.46715 | -44.93979 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c7e7b56-9f75-32ca-a7f0-6c504002d824 | -6.04271 | -44.13836 | 2025-10-13 03:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4c3e76ae-134a-3457-aede-6db768126003 | -6.74998 | -42.16476 | 2025-10-13 03:53:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8556244a-fc4c-3b43-b713-b6776dd5c55b | -4.285 | -48.5773 | 2025-10-13 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 019feb8f-1224-3add-9843-ebf1c9f7418f | -7.69519 | -42.37492 | 2025-10-13 03:53:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 19b5f514-9831-312c-ba37-fee105a4b050 | -6.45027 | -44.24711 | 2025-10-13 03:53:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd36820d-9046-3759-9812-55d3d695a963 | -5.39658 | -40.97306 | 2025-10-13 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8836626b-81b8-3b87-b2ac-dc42fa021662 | -5.3486 | -43.42073 | 2025-10-13 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa3b89bc-4780-31ab-9aba-e4158866594a | -5.57014 | -45.27795 | 2025-10-13 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| f1a02d2d-bd7d-3ed2-98ba-75450f19de00 | -5.94406 | -42.29279 | 2025-10-13 03:53:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 03523c9f-8f20-3b2f-aff0-d9672d74709e | -5.47955 | -44.65978 | 2025-10-13 03:53:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 59c09582-2563-3a37-8b8e-71ed4179d475 | -5.11278 | -43.20358 | 2025-10-13 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a0f60fa4-de6a-3010-b47a-d87ca92256d0 | -4.28412 | -48.57339 | 2025-10-13 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d83d2fce-63b1-3f5f-a9bb-b74c76f0fcd5 | -6.21891 | -42.48865 | 2025-10-13 03:53:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 04371833-2bec-3443-b091-4d265ef68716 | -6.26923 | -42.91287 | 2025-10-13 03:53:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d9eb19db-c838-3cd3-8856-7f79e275f973 | -4.47798 | -44.93177 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b33530b5-3195-372b-a5e4-2f86bfaa83e5 | -5.32037 | -43.43895 | 2025-10-13 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 543cf5ba-45b6-31fc-9e73-23db2c15e7d0 | -4.86871 | -45.73357 | 2025-10-13 03:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82b453da-c13a-3e12-b5f2-e5e7f5eb148f | -6.70343 | -45.97553 | 2025-10-13 03:53:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92d7239b-063f-37ed-a061-2ac92f816bc8 | -4.88434 | -41.49468 | 2025-10-13 03:53:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d4bdb133-bcbc-3bbc-9237-53ddbef28de1 | -6.32841 | -42.77156 | 2025-10-13 03:53:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| aa7a80d8-6f34-38c4-a555-ab900e043e89 | -5.84304 | -41.53214 | 2025-10-13 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 14d1e9c2-5e58-3032-a5d6-e2add2a583cc | -4.48317 | -44.93031 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a19737f8-f2f7-3a81-ba4d-9ae5593625d2 | -5.57095 | -45.27314 | 2025-10-13 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e48801e5-d606-31af-9781-db6e85605cf4 | -6.48174 | -42.0555 | 2025-10-13 03:53:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 722195b5-4400-3f25-8f5a-93d34aa0248f | -7.64686 | -42.57547 | 2025-10-13 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 563ff94d-4d4e-37fe-a83e-622a8990e64d | -4.67371 | -43.12797 | 2025-10-13 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| ac44f169-d9e2-315b-b9ed-f7b328f4bd87 | -2.9231 | -48.30182 | 2025-10-13 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c8d9c5b8-02af-3aa8-a81d-dcd29eb61d83 | -7.51526 | -42.16699 | 2025-10-13 03:53:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 710ef552-66ea-3cea-abb5-5799e2a8bc19 | -4.88798 | -37.50079 | 2025-10-13 03:53:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 27.7 |
| 57e22ec0-f5b6-33cc-89d0-68d6bb64fc29 | -6.8238 | -44.6557 | 2025-10-13 03:53:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55a5c75e-8de6-3932-ba38-416c008884f5 | -7.34076 | -43.86105 | 2025-10-13 03:53:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| faefccc2-373c-3e17-bced-4a24a9cbb792 | -5.81718 | -44.03237 | 2025-10-13 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 138ce69a-5596-3ae7-a9f3-9ddbee7b6436 | -6.233 | -43.00951 | 2025-10-13 03:53:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5b204b1a-8389-326e-a9c2-dbd187fc89a4 | -6.40522 | -41.95095 | 2025-10-13 03:53:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0534fd2e-f0be-32a3-a896-afb8326679b5 | -6.58047 | -45.97382 | 2025-10-13 03:53:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27ee1b2b-8342-3e31-9d6b-478c6b5a8655 | -7.34833 | -44.08377 | 2025-10-13 03:53:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0282a128-0299-346b-9e89-e9e8272a0f68 | -6.40862 | -42.53989 | 2025-10-13 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 56304458-cd20-3f1a-8038-2b5eec97cf6a | -7.1427 | -42.49635 | 2025-10-13 03:53:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d0e1cdbd-49c7-34dd-9056-04d23f22ffda | -7.69962 | -42.3711 | 2025-10-13 03:53:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 640d4a30-53bf-3380-ba5a-164532bfeb95 | -7.2705 | -44.15348 | 2025-10-13 03:53:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87be8469-133d-3421-93bd-10b3020d112e | -5.35677 | -43.42218 | 2025-10-13 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62da2803-28c0-3fcb-ba44-ea8014d60957 | -4.54972 | -43.99819 | 2025-10-13 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d63f9e47-4eab-3dda-b952-391e030a915c | -7.48422 | -42.75935 | 2025-10-13 03:53:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0efd7132-3011-3fd6-b78f-77d836dbb509 | -4.4778 | -44.93429 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| c82d8f65-32bf-3282-9b3a-04de81d260e0 | -4.48016 | -44.94677 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| adc6df78-6028-3bef-9a21-55becee5af7a | -7.28295 | -41.95808 | 2025-10-13 03:53:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c6407d4d-1a4e-3f78-bab2-50023062cc14 | -6.48543 | -42.05617 | 2025-10-13 03:53:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d364b212-1552-3e1d-9706-028672d622ea | -3.13356 | -50.2049 | 2025-10-13 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c698df3b-8968-34fd-9fb9-615187282a41 | -7.37978 | -44.07409 | 2025-10-13 03:53:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1a3fcc6-de15-3cb8-958f-fc37e24ac9bb | -5.53499 | -46.49085 | 2025-10-13 03:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6c09c8a-c501-3770-b5a4-254317b77cf7 | -5.24626 | -45.59618 | 2025-10-13 03:53:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26420db3-d25a-3a98-9a5c-4851172ba029 | -5.9007 | -44.73632 | 2025-10-13 03:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4ae738ae-cd0f-33bc-bb94-c2e42d0f4589 | -4.87161 | -45.91327 | 2025-10-13 03:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f479a00-791e-3104-93b1-b7c99395abfe | -5.91686 | -45.43378 | 2025-10-13 03:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7c7c6411-4253-3809-ab2c-c1edfe0de2f6 | -4.28928 | -48.57853 | 2025-10-13 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 80fb226d-2e46-301a-972c-1112cafa6977 | -5.92062 | -45.43148 | 2025-10-13 03:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8c0e4ab5-d46f-39fc-8ec0-dcd973abf3b1 | -5.32444 | -35.93209 | 2025-10-13 03:53:00 | NOAA-21 | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b145e6b8-f6ac-3200-b5c7-ee0e27e8e619 | -2.24779 | -47.87598 | 2025-10-13 03:53:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d0c0f969-398c-3299-ac8c-666a60024463 | -6.77704 | -42.82188 | 2025-10-13 03:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a3623e22-ac46-3f47-9f7f-914ddaa49d57 | -5.27327 | -43.39364 | 2025-10-13 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a4ac09cc-641b-3697-ba3a-ef6972fc6d0e | -5.91597 | -45.43074 | 2025-10-13 03:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af27c5da-7450-3f4d-b087-6feeb2027a64 | -6.17123 | -42.53952 | 2025-10-13 03:53:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| b0c5e7d3-13fb-37cd-890a-96ab9b013f4e | -5.41717 | -40.98055 | 2025-10-13 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1191eceb-f24f-324d-b0e3-3596beeab9a4 | -2.54621 | -47.80276 | 2025-10-13 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c799b2cd-5ecf-34b6-9520-230c25d171d6 | -4.47175 | -44.94057 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| a9345b59-cb4c-3f15-a1ac-7d61906150c5 | -5.44446 | -37.64491 | 2025-10-13 03:53:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README8.md)
