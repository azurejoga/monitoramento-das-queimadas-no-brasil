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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4cb0ca9-1fb3-3c52-8356-f1cf2b555d14 | -2.67225 | -57.59663 | 2024-09-27 04:38:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7228695c-14ae-3fb1-a2ea-51fd2bca4ca9 | -2.67172 | -57.59991 | 2024-09-27 04:38:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40ca8b0d-22ad-3fc1-9b03-151b5e799c39 | -2.66873 | -57.51911 | 2024-09-27 04:38:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6316ab9-4edb-3ba2-a1a3-b9a1e523b399 | -2.66293 | -57.52149 | 2024-09-27 04:38:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3d6c16b-9f77-3d48-b51d-ef2b2942cb9d | -2.66239 | -57.52474 | 2024-09-27 04:38:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea0d0715-7a79-307f-b6c8-53ecbc7ac891 | -3.6297 | -58.5619 | 2024-09-27 04:38:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 34e0a098-a918-3cbe-b311-69a22293e29f | -3.62909 | -58.5656 | 2024-09-27 04:38:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 77d5f76b-e8f9-3b8e-80d8-9ee1e8f6956a | -3.62889 | -58.56176 | 2024-09-27 04:38:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| fd5ed687-fba4-3f37-8715-a4830a256016 | -3.62825 | -58.56545 | 2024-09-27 04:38:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ffb46417-d7ae-3840-a405-5a316b2d0277 | -3.12328 | -59.13647 | 2024-09-27 04:38:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14c38161-2c35-3549-9905-fb13c0932c68 | -3.12258 | -59.14059 | 2024-09-27 04:38:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0dc29c94-a536-39ba-8012-e651bb5d2d53 | -3.01952 | -61.68983 | 2024-09-27 04:38:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8230d45e-9fac-3733-9adc-ac7bf4229bee | -3.18128 | -50.28909 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d5a0d47-a009-3f8b-a13c-436c981f75d3 | -4.33038 | -39.13664 | 2024-09-27 04:38:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b4554b18-c362-3a33-9944-a719c53e428f | -4.32984 | -39.14035 | 2024-09-27 04:38:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ed0430fd-84b6-3edc-9293-672d12816847 | -6.61543 | -39.59042 | 2024-09-27 04:38:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3289080f-42af-3295-a306-8d328676fead | -6.61039 | -39.58551 | 2024-09-27 04:38:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8d0904f4-d837-351b-a574-bc84f61f1506 | -6.10444 | -41.78708 | 2024-09-27 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 58d049b5-c83a-3efe-8077-d3003f7ef8ed | -6.0996 | -41.7869 | 2024-09-27 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ad60aab7-a174-3b0c-aaf1-9ba668ef9982 | -5.65368 | -41.24626 | 2024-09-27 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 35a60c4e-ef2d-3af5-b6a1-63e6d843bd3a | -5.11174 | -40.81422 | 2024-09-27 04:38:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5354d520-77ce-353d-a88d-74975efc0b51 | -5.11117 | -40.8143 | 2024-09-27 04:38:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 68930b50-e666-359e-9ae8-95a48f8b61b8 | -6.79137 | -41.23994 | 2024-09-27 04:38:00 | NOAA-21 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 73264332-cf58-3f32-8bc7-0c9abd15bb40 | -6.79097 | -41.24286 | 2024-09-27 04:38:00 | NOAA-21 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ce81a34a-9bbb-3f3e-890e-1080ccb4ca03 | -6.78593 | -41.2423 | 2024-09-27 04:38:00 | NOAA-21 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 20cf46bb-f356-3689-8253-b86b1630ac14 | -6.78131 | -41.23876 | 2024-09-27 04:38:00 | NOAA-21 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| be66d590-6b85-3e48-b4ca-6caa90ab2387 | -6.78092 | -41.24161 | 2024-09-27 04:38:00 | NOAA-21 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 184b62fa-ac09-33bc-8b37-cb930e6a25f4 | -3.21796 | -42.6856 | 2024-09-27 04:38:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e537e13-6d25-3f2d-89b0-cfa91495b8ab | -3.21618 | -42.68751 | 2024-09-27 04:38:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 76b98947-7f49-3de8-a036-ec416cdf0cb7 | -4.79812 | -43.04727 | 2024-09-27 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d0a149cb-a1d8-3fbc-a09f-81e22adbf7c0 | -4.79383 | -43.04663 | 2024-09-27 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 22470b56-52d1-35d0-9fdf-9fc902c27abd | -6.01578 | -42.71008 | 2024-09-27 04:38:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 68414909-6432-3cfe-bf70-106f1c5cec32 | -5.9889 | -42.55952 | 2024-09-27 04:38:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ce5f8918-fe8a-347b-8aae-c09ee9665a4e | -5.95423 | -43.27255 | 2024-09-27 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8b23f5dc-1056-3e12-9870-fae4d5b18ba5 | -5.94994 | -43.27187 | 2024-09-27 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 2e5a2a50-54df-38a4-85f4-3f93afd33c1b | -6.41243 | -42.92614 | 2024-09-27 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 72a8ce6f-890e-3434-a245-448ffc21a69b | -6.32985 | -42.50452 | 2024-09-27 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 147ccb9f-c251-30d5-8506-588171f4001f | -6.32599 | -42.49902 | 2024-09-27 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 05eaf002-f36a-30aa-a9e5-266f3b58d888 | -6.32532 | -42.50362 | 2024-09-27 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7377610f-3498-3f60-b01f-e49fb683e486 | -6.32144 | -42.49821 | 2024-09-27 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2dcb4538-ad82-3f2a-91ea-10649ee30d45 | -6.31691 | -42.4973 | 2024-09-27 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 370414ad-9fee-34c5-a338-e11315f527e1 | -6.31172 | -42.50104 | 2024-09-27 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9b061eaa-6330-3ee9-85f9-92b4f2b1552f | -6.30714 | -42.5005 | 2024-09-27 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ca8eebdc-8ae5-30b8-8966-c27c5ccd046f | -6.30647 | -42.50522 | 2024-09-27 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9836fd77-6b2b-3356-a98d-7b8f7c4f2cdb | -6.30191 | -42.50458 | 2024-09-27 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 24d085e7-5a22-3d07-8514-75afde4eb921 | -6.29737 | -42.50378 | 2024-09-27 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 2a46ac7c-6ac1-3117-840a-a0b4976d29f2 | -6.29672 | -42.50835 | 2024-09-27 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 433f9955-b35e-3e0e-b5ab-4d5fcf49e6e1 | -6.28699 | -42.41005 | 2024-09-27 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 46c2bf8b-90d6-32e0-ac92-8b309b533bd0 | -6.28626 | -42.54951 | 2024-09-27 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8e54ed47-4aac-35ce-8482-73ba096d1990 | -6.26529 | -43.13612 | 2024-09-27 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 11528b87-afd5-304a-af8a-d3ca25640f24 | -6.33431 | -43.1588 | 2024-09-27 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15f52b62-6b83-326c-acb3-64aec24c109a | -6.3337 | -43.16304 | 2024-09-27 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d4ca41a-30b7-3a0d-babb-5ae5020cc33d | -6.3292 | -43.46525 | 2024-09-27 04:38:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 379748c4-2e14-3e99-9cdb-a89353972776 | -6.32874 | -43.16656 | 2024-09-27 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c6d5b1b-bad2-3dfc-baa7-4ce1290a6f73 | -6.32494 | -43.46456 | 2024-09-27 04:38:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c368a992-4d33-3c68-a9e1-fa0857603165 | -6.23464 | -43.31438 | 2024-09-27 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94a4ad27-f80b-3a59-b0d0-b0a11b1b71ce | -6.23403 | -43.31853 | 2024-09-27 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcae14d5-8c30-3911-a269-0aaff1fcea25 | -5.88094 | -42.14034 | 2024-09-27 04:38:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 11a898cb-db1e-311c-a4d3-b064a0b482fe | -5.87959 | -42.14122 | 2024-09-27 04:38:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 46bde531-6243-3f29-8242-503e74bcceec | -5.74691 | -42.61369 | 2024-09-27 04:38:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1626e36f-37f0-3fc3-ba25-f0d6fc848355 | -5.58413 | -42.93301 | 2024-09-27 04:38:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| f7f935ce-7502-3c9f-b5ef-e58f7915b5ab | -5.58354 | -42.93716 | 2024-09-27 04:38:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 30.6 |
| 6c4d59c0-372c-3051-81ec-43cbd133ee58 | -5.57975 | -42.93238 | 2024-09-27 04:38:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 7452859d-0407-3db5-9db2-0f03cfa8667a | -5.57915 | -42.93654 | 2024-09-27 04:38:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| e84b7f90-995a-325a-9df4-111c54ead933 | -5.57856 | -42.94071 | 2024-09-27 04:38:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 0f90a2d9-61be-35fa-8097-9c422551c56b | -5.31154 | -43.08063 | 2024-09-27 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d8a6c70-498a-36de-afbe-3c1ac584602b | -5.30912 | -43.08124 | 2024-09-27 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7da17a6d-6e3e-3994-a00b-280365771d32 | -5.30174 | -43.07156 | 2024-09-27 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f57010dd-4ee0-3010-832b-4bf254e483a1 | -6.64797 | -42.0906 | 2024-09-27 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5bf31732-641b-3ab8-9879-2e339e717edf | -6.5556 | -43.1529 | 2024-09-27 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| df4d2629-706a-362f-bb51-d7340894c00c | -6.55499 | -43.15717 | 2024-09-27 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e905ec08-84f1-3fc9-a6f0-2e0ea159baf3 | -6.55122 | -43.15228 | 2024-09-27 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aafecf43-38fd-32c4-a7bb-d5e97186b749 | -3.53756 | -43.55819 | 2024-09-27 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8edab9e1-4d0e-3cd6-9884-9764161fede9 | -3.53349 | -43.5576 | 2024-09-27 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67c8639e-c60c-3afa-8a7c-260bba021f3b | -3.48847 | -43.35731 | 2024-09-27 04:38:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9843ce2-9c5f-35ec-836f-1039a1653ff5 | -3.48792 | -43.361 | 2024-09-27 04:38:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 248d191d-ded1-3003-a2d5-78cfac18387a | -3.48435 | -43.35668 | 2024-09-27 04:38:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8d1e7ec-3621-3301-b155-7470305b6c34 | -3.48379 | -43.36038 | 2024-09-27 04:38:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f6e5bb3-8b8d-3491-9902-85deb66fe1f1 | -3.25597 | -43.0576 | 2024-09-27 04:38:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d201f5d1-9700-32e7-aca0-2d5542865761 | -3.25238 | -43.0531 | 2024-09-27 04:38:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c137935-67d2-3ace-9e56-0472678fb65c | -3.25179 | -43.05693 | 2024-09-27 04:38:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ddf4c9de-d4ef-346c-9566-8e1368436d72 | -3.35496 | -44.18872 | 2024-09-27 04:38:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97c93eba-5e91-3206-bae0-636837d1907e | -3.35422 | -44.19365 | 2024-09-27 04:38:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 313ca557-3c9d-3d93-846d-945e47f13701 | -4.66568 | -43.75916 | 2024-09-27 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08af1fbb-0539-3f67-a676-a1b9d6e6d1e3 | -4.6616 | -43.75852 | 2024-09-27 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11fb1ae0-998c-3d2d-b680-5e5c8c0ed877 | -4.66105 | -43.76216 | 2024-09-27 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 478967b7-110d-36b2-be9a-ec0fe1b36d42 | -4.66097 | -43.81757 | 2024-09-27 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 32018484-d81a-3ff2-bd20-e2de05fe4c66 | -4.65698 | -43.76149 | 2024-09-27 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bca9737a-584c-3eb3-8af0-68db4b1bf40a | -4.54301 | -43.57489 | 2024-09-27 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb84a5b5-cea6-3c59-a1d2-126077e8229e | -4.54245 | -43.5786 | 2024-09-27 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c28f214e-1732-3338-8712-8d6b3ecf23da | -4.0389 | -43.24044 | 2024-09-27 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0a53ab3-2fe7-3c89-9e18-369d1ec394a2 | -4.03832 | -43.24432 | 2024-09-27 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a122abd-bf63-331e-ba2a-9d85bbe4b292 | -4.03471 | -43.23981 | 2024-09-27 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8bff2fd-7118-38da-b9c6-54bd7711a3f6 | -4.03413 | -43.24369 | 2024-09-27 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c849338-9086-3f15-9347-4c0b74f2a84e | -4.03052 | -43.23917 | 2024-09-27 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba40e2ac-8f4f-328f-9e1a-7408eac30f33 | -4.05887 | -44.0499 | 2024-09-27 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e4e60f9e-8c94-3feb-a16f-e1d408ad93e8 | -4.05836 | -44.05329 | 2024-09-27 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9c4e2d43-8cab-3042-bd32-f73e04081e54 | -5.02695 | -43.79262 | 2024-09-27 04:38:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| cec9f682-2be9-3cc2-a61b-29a93fc42cab | -5.02641 | -43.7963 | 2024-09-27 04:38:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| dd5b0eaa-afb8-3cd8-a0ce-7c5af2408124 | -5.02285 | -43.79202 | 2024-09-27 04:38:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |


[Clique aqui para ver as próximas entradas](README71.md)
