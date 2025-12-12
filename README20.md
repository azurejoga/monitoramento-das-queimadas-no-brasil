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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b79f88f9-046b-30db-9fa0-3edb642e7eed | -2.4367 | -51.948 | 2025-12-12 04:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 18489286-fa13-3b01-a215-be7b532bf5e2 | -14.8941 | -58.1282 | 2025-12-12 04:30:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 93513e9e-076d-31ed-b205-f55da087ee13 | -12.3946 | -58.0307 | 2025-12-12 04:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 56820275-5881-34f9-acf7-fd3a245e715a | -2.3565 | -54.3831 | 2025-12-12 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 4c0e615d-3c5c-3d5f-b90b-dbd82673b330 | -12.4133 | -58.049 | 2025-12-12 04:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| fae1ac3c-2983-3650-ac03-2406aa950391 | -12.4135 | -58.0292 | 2025-12-12 04:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 7c9154da-08d0-3dfe-81d6-d1ba086e4371 | -2.4183 | -51.9484 | 2025-12-12 04:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 59adf6c4-0741-3a71-862d-f584ecea8eb5 | -12.3943 | -58.0506 | 2025-12-12 04:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 9400f477-8890-31a5-ba3e-1fa2cf70ca9b | -2.4183 | -51.9484 | 2025-12-12 04:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| ec21b228-d59a-3181-a5e8-66cbd3fe1ec4 | -2.3565 | -54.3831 | 2025-12-12 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 227f1ce0-32c1-3454-8cda-dacbdd85a682 | -2.4183 | -51.9278 | 2025-12-12 04:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| af0f6d59-13b4-3e7e-b98a-d2ab37f1fc23 | -2.4367 | -51.948 | 2025-12-12 04:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 92ddef95-2c51-337a-bfc0-8b131a5a1901 | -2.4367 | -51.9274 | 2025-12-12 04:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 132.6 |
| ddd4a51e-39f3-34a1-a19f-8ab12150b3f1 | -14.8941 | -58.1282 | 2025-12-12 04:40:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| e7cc10e1-5035-33d0-8f2c-23dda9edf72d | -4.0392 | -42.3475 | 2025-12-12 04:40:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 67.1 |
| 4905c3ff-63e3-3170-814d-f8eab45c734b | -2.3566 | -54.3631 | 2025-12-12 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| d5c6a7c7-2904-3560-8361-cd1d3f487eb4 | -14.9134 | -58.1263 | 2025-12-12 04:40:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| bb582210-1b48-361a-a3e6-1ef6c4fd6445 | -14.9134 | -58.1263 | 2025-12-12 04:50:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 474dc76c-8fdc-3310-87ff-431a57dc3e05 | -2.4367 | -51.9274 | 2025-12-12 04:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 55297244-99ee-37e1-ba70-716745096df0 | -14.8941 | -58.1282 | 2025-12-12 04:50:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| abeb5a01-2b1d-3db9-b655-81d897b38c5d | -2.4183 | -51.9278 | 2025-12-12 04:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 37204974-d1b6-35c4-9bb4-7c8ac2d6e596 | -2.4367 | -51.948 | 2025-12-12 04:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 0f200b6b-8098-31d5-8f07-61e62b6bc8b3 | -2.4183 | -51.9484 | 2025-12-12 04:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| d16a01ca-b49c-38f6-b217-21f6d79bc132 | -2.4183 | -51.9278 | 2025-12-12 05:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| e8c34b3f-c1dd-3942-b0ab-464f2c20200f | -12.4133 | -58.049 | 2025-12-12 05:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 74621b5a-f88f-396a-988a-a5710d9f1cbf | -2.4367 | -51.9274 | 2025-12-12 05:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 5a572edf-9896-3da2-b209-7c8eff9f8b92 | -14.8941 | -58.1282 | 2025-12-12 05:00:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 93973dde-adb7-3b01-bfbd-012158cb95cb | -12.4325 | -58.0276 | 2025-12-12 05:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 49889f4e-0853-3d74-84b6-fdd942b147e0 | -2.4367 | -51.948 | 2025-12-12 05:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| eda994da-43c3-3d96-a891-543b871ea7ca | -2.4183 | -51.9484 | 2025-12-12 05:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 98deb3cb-3ee7-3ffd-8eb3-cd5ebcafed8e | -2.5108 | -51.8023 | 2025-12-12 05:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| e62ec17d-9dd9-3a2e-b655-17ac6df5f97e | -2.4923 | -51.8027 | 2025-12-12 05:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 3d505aa0-f32c-3f39-846f-258d6c759dec | -12.3946 | -58.0307 | 2025-12-12 05:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 43.1 |
| b018d2dc-a402-3c29-b460-cb1dd487a108 | -14.9134 | -58.1263 | 2025-12-12 05:00:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 5b9313b4-707d-3d2a-9d94-9f81bb70d74d | -12.4135 | -58.0292 | 2025-12-12 05:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 649df0a5-a085-31d9-8082-b00f113e6f2f | -12.4323 | -58.0475 | 2025-12-12 05:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 367c60c5-d623-3992-9270-9df2ccd0e6ab | 2.03391 | -61.42143 | 2025-12-12 05:08:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5bb1cba-4c74-3ff0-9281-880a0520c3fd | 1.99621 | -55.67409 | 2025-12-12 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 710e967c-806e-3258-9e43-dc5e1b532fc1 | 4.29945 | -60.8637 | 2025-12-12 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c613c17-5784-3dab-8478-3251a948ae2d | 2.90949 | -60.92205 | 2025-12-12 05:08:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea49d517-1477-38aa-ade5-cb74a85d859b | 4.11923 | -60.67158 | 2025-12-12 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d80074f2-601a-3038-b729-7a932b5b591e | 2.02837 | -61.41402 | 2025-12-12 05:08:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c50ac0bb-6ff5-3f10-b11f-5627b5fab96e | 3.21991 | -61.19842 | 2025-12-12 05:08:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7329d8e1-000a-3692-886b-9bb3d931ae88 | 4.30005 | -60.86767 | 2025-12-12 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bacf1adc-3c62-3d9d-8c4c-4f6714291499 | 2.03277 | -61.4214 | 2025-12-12 05:08:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3ee2e74a-27d0-34c1-b5c3-9cf4e8f73e83 | 0.10165 | -51.12791 | 2025-12-12 05:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ab98cbc1-b5ce-3419-8de9-789653385b98 | 2.02962 | -61.422 | 2025-12-12 05:08:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02f0cf96-ea74-35e9-9d1d-51e6a3165870 | 2.029 | -61.41802 | 2025-12-12 05:08:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9492c864-5639-3be4-81ad-ddd6518f705f | 2.03328 | -61.41742 | 2025-12-12 05:08:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf8d7ac8-c02f-377a-aa46-8ee021b80cda | 4.29888 | -60.85991 | 2025-12-12 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8153da06-2de1-3c73-bc5d-4f971748a7de | 1.99575 | -55.64959 | 2025-12-12 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b086012-9485-3ad8-9225-9752a8b70e21 | 1.99291 | -55.67459 | 2025-12-12 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4f2bef46-9b93-3193-817b-16c91e8df90a | 2.03157 | -61.41335 | 2025-12-12 05:08:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 67fc9f2c-13bf-31bc-97bf-fd3d034f5892 | 2.03217 | -61.41737 | 2025-12-12 05:08:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 08eb5125-6a00-3de2-a0e4-229eaf7f4d0e | 3.2193 | -61.19438 | 2025-12-12 05:08:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f596db52-7b2e-3480-87ee-f3f0ee20a97f | 3.93791 | -59.90973 | 2025-12-12 05:08:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12ab1212-3aaf-30fb-b23f-83e3f908f42f | -2.4183 | -51.9278 | 2025-12-12 05:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| db527859-e116-342a-a9f7-0699f9ea8f7d | -14.8941 | -58.1282 | 2025-12-12 05:10:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| dedfc17e-e857-3234-bb16-1820ebd6941b | -2.4367 | -51.9274 | 2025-12-12 05:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| dfd7d0bf-9b06-3ce5-b368-638b8b02db1f | -2.4367 | -51.948 | 2025-12-12 05:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| c1240c5f-eabd-3a4e-bea0-1d4f9c7c0979 | -2.4183 | -51.9484 | 2025-12-12 05:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 3cd17025-b49d-3d19-a049-2ccdbe4deb1b | -14.9134 | -58.1263 | 2025-12-12 05:10:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 8c3eeca5-e65e-31e6-aecb-80046d3ecbe0 | -3.23152 | -52.63963 | 2025-12-12 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe9d17ed-0da9-3312-8247-333652c5b5c2 | -1.11541 | -53.689 | 2025-12-12 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2625e15c-15fd-35eb-97ad-8adf54a727f1 | -0.29857 | -50.41817 | 2025-12-12 05:10:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2942da9e-2113-3737-8ddd-ca22f4ded5af | -1.79221 | -52.14714 | 2025-12-12 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee78177b-8322-3a80-8ab1-ead859233da6 | -2.22512 | -45.40374 | 2025-12-12 05:10:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c44b7273-d21a-3b36-87cc-6ef16546f79d | -2.88454 | -53.0136 | 2025-12-12 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 11ba8432-6285-3c13-82ca-54c80d786626 | -6.62779 | -55.02069 | 2025-12-12 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0765556-3ffb-307c-9826-8f953068b568 | -1.38019 | -53.22441 | 2025-12-12 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e766d1f5-f698-3c1e-8996-9ee0c95680c4 | -2.26413 | -51.93297 | 2025-12-12 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f337c4b2-1ea5-3440-8128-a74dec85af8a | -1.75776 | -54.03905 | 2025-12-12 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ac2bc6ee-84dd-3b46-a2d0-ec1847522dc6 | -3.74355 | -55.99117 | 2025-12-12 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a446e83-ec06-30fc-b5a6-5537aa17bca0 | -2.60051 | -51.93813 | 2025-12-12 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81a592bc-1bfe-36c9-a6bb-ee090b649ffd | -2.83772 | -46.73431 | 2025-12-12 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d2c31a8-a8c3-304e-a6d8-1d43812abd43 | -1.70343 | -52.14531 | 2025-12-12 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2d271d5-2213-3803-bf1a-af7f9d5bef61 | -1.54678 | -55.70598 | 2025-12-12 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8e78611-2aa8-3938-9907-b6b40eea99e9 | -2.83973 | -46.73442 | 2025-12-12 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d133dcb-c116-38fe-9417-caac6b4e5190 | -3.01639 | -52.83281 | 2025-12-12 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bdbea88-1723-33e0-a1c1-4ae9c4d3d713 | -1.48931 | -55.48698 | 2025-12-12 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e6b7171-0677-3b2c-924a-f25c06db1f9b | -2.43221 | -51.93609 | 2025-12-12 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ed855c7a-31fb-331f-acc7-980dee265e05 | -3.49941 | -52.52955 | 2025-12-12 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 840c9b21-24f1-3c6e-b6eb-ee79a9776019 | -2.7803 | -54.52737 | 2025-12-12 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7aa2164c-35d4-3668-a94c-e5d75b956b46 | -3.38659 | -47.18767 | 2025-12-12 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76c42387-39b3-3d93-87d7-947df6e81c6b | -2.51465 | -47.81202 | 2025-12-12 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5dd9a2f-0a05-3bd4-a886-177140705efb | -2.23051 | -45.40919 | 2025-12-12 05:10:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 193df189-2efa-3c19-a245-189a2d4e0672 | -3.13149 | -54.17807 | 2025-12-12 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c35def0e-4d76-376a-ac95-9c945f3de1e8 | -3.17433 | -52.42426 | 2025-12-12 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0e57f2d-2697-3bb6-9dd4-b0d5a1a1260b | -3.37303 | -54.11308 | 2025-12-12 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45de1c41-b6bb-32d9-9dde-fab4044d8fb3 | -4.84827 | -45.5233 | 2025-12-12 05:10:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 072068a4-5637-3dcc-9849-70ad2c4f4df8 | -2.43766 | -51.92667 | 2025-12-12 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 9b42596d-8559-3e8d-9457-20f18c65ead9 | -1.29226 | -53.16169 | 2025-12-12 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c04b1981-b840-3cc0-9de9-fd79ba8cbdfb | -2.93931 | -53.0266 | 2025-12-12 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7defd014-f7a5-3b07-95b4-4bf4762d675a | -2.43636 | -47.19486 | 2025-12-12 05:10:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f760e032-97ca-368b-ac68-3c86d51353d8 | -3.05025 | -53.01084 | 2025-12-12 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5b62aa2-2aac-3b3e-9c21-fd64925711d4 | -4.84654 | -45.52299 | 2025-12-12 05:10:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d1e0be6-d058-37fe-866e-706537266558 | -3.36723 | -52.74061 | 2025-12-12 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e5b2603-878b-373b-9191-c7ff7acc9ce4 | -3.17626 | -52.87321 | 2025-12-12 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 809fa239-c6a7-3737-9552-42e3792a5352 | -2.49792 | -51.7973 | 2025-12-12 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 60b60467-3242-32d8-837b-c107257eff1f | -1.19601 | -54.17963 | 2025-12-12 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README21.md)
