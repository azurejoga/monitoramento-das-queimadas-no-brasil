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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba78e253-7c9c-3c4e-b639-382061f565cd | -11.19176 | -45.71979 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 79fd43f1-ee60-3f23-85bd-405193109a1b | -11.19132 | -45.73613 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ec0ade7b-710a-3eff-98a3-036d621b5d80 | -11.19111 | -45.72324 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2616398d-59e1-3491-83c8-9da1d087354e | -11.19067 | -45.71096 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb23ea1f-28ed-39b3-8cf4-447067a3f4ec | -11.19065 | -45.73956 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71db050e-fa09-3526-b0b7-3683d592f98e | -11.19046 | -45.7267 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e1f447f7-699e-3c57-90e9-e46e2d3bdcc4 | -11.19025 | -45.69823 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 367a4303-ab85-358a-8f0e-2158aef13445 | -11.19001 | -45.71437 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| db39b986-5484-3755-bc12-7f6f3cdd00e5 | -11.18998 | -45.743 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9dedfabf-2820-3527-8dd3-dca2a30f5d9c | -11.18981 | -45.73016 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d1416cfc-d7eb-3d09-9baf-7f1ae220fe0a | -11.18934 | -45.7178 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c492614d-e21b-3556-b6a2-f7132c195bba | -11.18867 | -45.72123 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c61c31e0-3409-3bb9-b1d4-7c9e918ec83a | -11.18835 | -45.70836 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 86bf32b7-5d1e-3433-ae15-c347f88abd68 | -11.188 | -45.72467 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 24c4e841-137a-3cbf-8def-571c098657f8 | -11.18771 | -45.71177 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 42899fd6-cc28-39ae-9b09-dbf893e53b7e | -11.18732 | -45.72813 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 39180294-3dde-3b85-ad94-2e9c8d3610de | -11.18723 | -45.74394 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 47f64a19-7cf2-3463-ae25-fa68025a46a8 | -11.18706 | -45.7152 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c9e48655-7c5d-34e3-afe7-43dc3258632f | -11.18665 | -45.73157 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 615dd9ca-98e5-38a3-a735-3a4c7ce3b246 | -11.18621 | -45.69024 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c97b1e11-5d61-3560-bda3-04a1ca30192a | -11.18463 | -45.74191 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a8a31b34-6e1b-37bd-9d10-e28542c55b83 | -11.18396 | -45.74536 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0399f940-5b9d-382c-9569-c2c4b98eb322 | -11.18346 | -45.67542 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ecaaa3bf-cc5c-34b7-b0c1-b7103d7f9e59 | -11.18281 | -45.67883 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 034fe958-ee07-369a-af28-2e1c5c046a4b | -11.18236 | -45.71071 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 340996b2-0b06-3086-b573-7609ee340c7d | -11.18187 | -45.74288 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 25365008-78f3-3fce-a104-a637d36a3db1 | -11.18171 | -45.71416 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 22bc8339-16c9-3542-af2d-f2afed426f7a | -11.18122 | -45.74634 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3ad84738-9bbe-3807-830f-b434b1bee6a5 | -11.17781 | -45.73489 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 597caeb2-bf99-38a5-848f-f3d9a95c354f | -11.17716 | -45.73837 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0549cc24-f8f4-38bc-9311-855eaf56f97e | -11.17586 | -45.74529 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 33e81af6-bc72-3861-b918-9c96705dac8f | -11.1752 | -45.74876 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dc4b963c-2405-33b1-a9a7-605af311c089 | -11.17235 | -45.61717 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99a7ba6f-802c-3fb4-b8af-e383eb1056e3 | -11.1718 | -45.73732 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bd17b8b3-c619-3680-93cd-63b91e942d86 | -11.17115 | -45.74078 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9b5e6024-d3e7-31a6-81f7-712812397fbf | -11.17049 | -45.74425 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 23628c1c-b4f7-304f-8dc9-d23b078859db | -11.16984 | -45.74771 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 1b6fdcf4-f674-3a98-bdf2-ee9e1b2d294f | -11.16918 | -45.75119 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e9940c25-b900-3e99-8432-7e4f4a340a87 | -11.16747 | -45.67212 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d369471e-debb-3ed7-838f-265b7066d0b9 | -11.16682 | -45.67556 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 341c58b7-340c-3967-90c0-7c6b6f2afd1c | -11.16646 | -45.61913 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebd09eb9-4c71-3ca5-ad59-dbfb58197cb6 | -11.16583 | -45.62247 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0fde3c05-d78c-357e-8503-9f3472d104e6 | -11.16578 | -45.73975 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 27e282f2-ceb1-38e3-971a-ad7e281ac319 | -11.16519 | -45.62584 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 71862e2e-6440-3ed5-b788-4532e5f55678 | -11.16513 | -45.74321 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| c4167424-f90e-3519-b1f5-6dced554ba5f | -11.16455 | -45.6292 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 57dd00e0-f74c-32f0-ad5b-c78b90b400ef | -11.16447 | -45.74668 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 618a70a9-c43b-361a-b91d-608da93a9c99 | -11.16382 | -45.75016 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d29028c4-2353-3ad0-b738-584fe4c29abb | -11.16342 | -45.66428 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 66663c31-15b7-36ae-97a3-073db58914b4 | -11.16316 | -45.75364 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d6343b55-51fb-312c-95f7-2cc7bc330890 | -11.16277 | -45.66769 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50d646db-575f-33dc-8a44-5a8ea2a28764 | -11.16213 | -45.6711 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 863ad9d4-c01d-380a-808d-d4ba15473067 | -11.16147 | -45.67455 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0df65c81-18c2-31fd-ba12-e12fa65961e1 | -11.16116 | -45.61798 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55c3478b-3402-30ce-ae97-e2c64730411d | -11.16052 | -45.62136 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a53682ac-0627-3d6a-b61a-3fafd9754dea | -11.15988 | -45.62475 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c601e5cc-0e83-324d-bb8d-aa202f5afe5c | -11.15976 | -45.74218 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1a47a11f-cea1-3105-8344-4252c17043af | -11.1591 | -45.74565 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2f7a3a3b-a60f-3940-932b-bcc7b884e06c | -11.15845 | -45.74912 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 231c2654-f96c-3f0c-8a94-70101c02084e | -11.15779 | -45.7526 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 81b89f75-d599-326a-bf57-3d80402739e6 | -11.15666 | -45.97155 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57bb18fb-4a0d-32c7-947d-516d9710b71f | -11.15617 | -45.96961 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10ea5647-6030-37fc-9eda-09d8b57daf96 | -11.15612 | -45.67355 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9699929c-21e7-32de-8bb7-f58f373e4d9b | -11.15585 | -45.61693 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad3acd79-2683-3956-924d-0ae3c09c7f89 | -11.1557 | -45.73424 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 05b588ce-aca1-34d6-9ae7-1c3b57f5bac5 | -11.15549 | -45.9733 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22856022-32b8-3cc9-b328-7805ce444f2b | -11.15547 | -45.67699 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ced027c4-f599-3a74-a401-3616b41bd23f | -11.1552 | -45.62032 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e5597e1-7ef3-33de-824b-dc68a9482df7 | -11.15505 | -45.7377 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b9085dbd-28d7-3d9a-8c03-953fd2676050 | -11.15481 | -45.68044 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3d01473e-09d5-340c-87f2-a90f9f6aa242 | -11.15455 | -45.62373 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74e0f48b-d840-3ad4-9aaf-3c728d5534b5 | -11.15439 | -45.74115 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| bfef42ea-8043-346b-9b87-2588e5a2b385 | -11.15416 | -45.6839 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a0ff7a1-ed3d-39b6-b3b5-f59868cb04af | -11.1539 | -45.62712 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9d87d03c-a7ba-3887-b9bd-e6cd4abad049 | -11.15373 | -45.74462 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8769c892-4540-3ed3-ba0c-850cb86f09ef | -11.1535 | -45.68736 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 189405b4-1a5e-3df3-9b73-73b87ec3eb3a | -11.15284 | -45.69081 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f1725863-d1ec-331d-b638-d6f713507977 | -11.1523 | -45.72285 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d0597f4e-900e-3b7b-b35a-695972618036 | -11.15165 | -45.7263 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e9da9dbc-7bfa-39fe-9c56-75c2ec60279a | -11.15116 | -45.97079 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e347526-74fe-3eb7-a1e1-bf30d924670f | -11.15099 | -45.72976 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0f4d3340-f505-3e0e-93b9-20bd2b9d9d51 | -11.15088 | -45.70112 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d27610a-a62a-3318-b530-bc9d323bb2e6 | -11.15033 | -45.73323 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6929fb18-1b43-373c-8a54-a8a81299dfc6 | -11.14999 | -45.97246 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 037ba685-dbd5-3208-bdc9-02cd00b990da | -11.14968 | -45.73669 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5d652edc-f401-3f54-a618-cf37e4910277 | -11.14946 | -45.67944 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7064e7e8-83ae-3a38-9348-9893f52f15fa | -11.14902 | -45.74015 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e551d48c-c95d-3d4b-af23-a674bc1354d3 | -11.1488 | -45.68289 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 1794f328-27ee-3585-8840-5766151af11b | -11.14836 | -45.74361 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 897796e8-2730-3c56-8d85-994255d97bde | -11.14815 | -45.68633 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| d7d3ab76-a0bf-362e-98f8-12811f56555e | -11.14791 | -45.62956 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 009c2071-c777-3ebd-b864-67f08abe01bf | -11.1477 | -45.74709 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e58f1954-83c6-3bed-92e9-84c968f36da6 | -11.1475 | -45.68977 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ec292d99-0ad5-352f-b731-6a5a78747c75 | -11.14726 | -45.63298 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09f38f11-17b0-33ab-8484-e2ddb3252d5c | -11.14684 | -45.6932 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e93fccc5-1df1-3fd0-9552-fd1578ab5ccf | -11.14628 | -45.72528 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 28fd5c23-939c-3b5f-a563-afe8ce410b5e | -11.14562 | -45.72876 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3ec9a3ac-ecae-3d5f-981d-e237ffd60d6a | -11.14553 | -45.70007 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7f5bf476-a3d1-3e4c-b730-dd826f75c146 | -11.14496 | -45.73222 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 68fdbca7-1e38-33be-b6eb-188880b9fa94 | -11.14488 | -45.70351 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |


[Clique aqui para ver as próximas entradas](README19.md)
