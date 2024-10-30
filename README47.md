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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8f9fcef-59a1-303f-b65b-a49740ff9d5f | -3.1316 | -54.26716 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a78a095e-1590-35d8-b6ce-95442690cbde | -3.12651 | -54.26219 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2afbaef5-605b-3616-b4ab-84ab7f438e33 | -3.12519 | -54.26997 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 92c7c9f8-c5ad-3045-8816-8b80ec9ee00a | -3.12451 | -54.27394 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fcfa14e0-5873-3d35-a9e2-9ce8ac4c6dec | -3.11874 | -54.27295 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d351356-3f2e-394c-8c02-65db683faedc | -3.11157 | -54.28012 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fb1aca4d-868b-3f8b-bc8b-684b83e267bc | -3.1112 | -54.27934 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9de780d1-a4f2-3e59-ae9e-b1d1862056bf | -3.11053 | -54.28343 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6d72b342-6548-3a6b-bcf9-224ff6d7a0f1 | -3.10649 | -54.27512 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ed195960-f497-348c-8815-a234c7b5153d | -3.10579 | -54.27919 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 14417c51-f581-3037-8182-2e6ec92d5662 | -3.10509 | -54.28327 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b69759b-50f7-3a6a-aa15-c32069bb0f18 | -3.10474 | -54.28248 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6e3eeaae-34af-35b7-95f5-4107d39f3fcb | -3.10407 | -54.28658 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f6fff54c-e037-335b-b852-cab8cd1bac0c | -3.10069 | -54.27426 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bd46875a-f9f9-3d2d-94c4-1d5c9dca04a4 | -3.10065 | -53.7144 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2aa6dd7d-433b-395d-840b-efbe0a99aa08 | -3.09895 | -54.28156 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 7f929013-d100-3c87-8971-13a03d4a1621 | -3.0986 | -54.28641 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 497bbeed-1a75-3e16-887a-b09daebea4ce | -3.09829 | -54.28562 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e100842d-5237-3b08-b02c-e725a8922a43 | -3.09443 | -53.71722 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3bbb7d60-c4b0-35ef-88b0-26d3080042da | -3.07663 | -54.16638 | 2024-10-30 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a5b9e889-57d7-3919-8917-d796624c5af8 | -3.07598 | -54.17024 | 2024-10-30 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2320ff4b-c4c6-374a-b764-7824f97dfe70 | -3.0709 | -54.16534 | 2024-10-30 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| dc42f072-bdb8-38eb-a0e5-d8b6627ed4a0 | -3.07025 | -54.16924 | 2024-10-30 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1b54f941-69ae-3260-bf55-9589860f02e2 | -2.2811 | -53.77773 | 2024-10-30 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34e4a0f2-4d71-3dda-b7ea-849a051f6abf | -2.27543 | -53.77682 | 2024-10-30 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db529c80-841e-397e-8265-3d2b6bb8dd0c | -2.24979 | -53.72124 | 2024-10-30 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76bad506-0d54-305d-9ead-f2b9718a2d95 | -3.59369 | -53.78528 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f56325a8-0a07-3046-8778-9f4fce2c50e3 | -3.46066 | -54.07836 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78618bcc-37c7-3747-a013-d262caa6ad68 | -3.46 | -54.08239 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40155fb1-c948-3fd0-bf4d-623a38410b1e | -3.45788 | -54.07544 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68609a23-9997-3a3b-86e0-951cf81bbd17 | -3.4572 | -54.07939 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8529ee59-7e0c-3f9e-b68f-bd1df63ea521 | -3.45651 | -54.0834 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09e2d6a6-a7aa-39ba-bbed-4ec40392fdef | -3.45563 | -54.0735 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 82cdc1dc-f336-3d94-b83d-d7e96cd4460a | -3.45499 | -54.07739 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 344533a2-8e89-37d5-b1e8-f0a95f43765b | -3.45433 | -54.08136 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cc2755e2-5963-31cf-ad1f-ce4a6e88fc80 | -3.4522 | -54.07459 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41cbccd5-c20d-3bdf-b31c-60acfe24160e | -3.45152 | -54.07849 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc7db2fc-5e11-3d7d-a0ea-b48318719d19 | -3.45084 | -54.08243 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26d0b25b-7fb4-3f69-b830-25a75095462a | -3.42711 | -54.15163 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e73ea772-2bca-3963-b71a-959fe656542c | -3.42544 | -54.14972 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92a79637-715f-3904-b1c3-2e17aec546bb | -3.42477 | -54.15374 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23917cd7-b65b-30de-a793-aeccc6b829de | -3.41909 | -54.15265 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab8cc3db-0e21-3e49-aa93-603ad7bda84a | -3.13226 | -54.2633 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e06687dc-eaa7-3e5d-a1e6-7aea2e190700 | -3.12585 | -54.26607 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c3f56090-2132-38f5-b130-6eb2ffcbcca2 | -3.12382 | -54.27796 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3102bab-4133-3aab-9c5e-1268d9bd858e | -3.1201 | -54.26497 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a3ad0904-755f-3363-96d7-f11038fde829 | -3.11942 | -54.26894 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| de860817-c64d-3cae-9844-b281d795cee7 | -3.11805 | -54.277 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 817b3269-ce1f-35c5-8615-3c25276e5600 | -3.11087 | -54.28419 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e26ca20b-ad04-3bca-8e40-76fc3216e236 | -3.10622 | -53.71531 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3539740a-4d03-330d-a54e-fc00dd6b1a37 | -3.10608 | -54.27431 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 97c3b4bf-797e-3468-a0ab-a5e0fb8e3ef5 | -3.10541 | -54.2784 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dbeba64d-4352-337b-9712-1145fa67648e | -3.10438 | -54.28735 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2ddb3ac8-8195-32ef-a523-68f9bf666893 | -3.10029 | -54.27346 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c10fc929-4e72-3c4e-bfed-883444bbd3b9 | -3.10001 | -53.71813 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23263751-5eda-3754-a105-e51524964e94 | -3.09999 | -54.27831 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 9317061f-060e-3174-92ca-5f48273ea27e | -3.09962 | -54.27751 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 2acc1856-4e53-3060-9a7a-825fec2edd23 | -3.0993 | -54.28236 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 14f6298c-e828-3708-95e1-3de6c40bc002 | -3.0979 | -54.29047 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 623664a0-97fe-3db8-8bc6-a93b0d7ba4e4 | -3.09762 | -54.28969 | 2024-10-30 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c9b88b4a-2646-36c5-8cde-70c8f55f1198 | -3.09564 | -53.81134 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de0236c9-f13a-35a4-ae55-27d0838d78a8 | -3.09563 | -53.71759 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c2cd83bd-dae6-31ec-a88a-b9f7d280dd9c | -2.28174 | -53.77387 | 2024-10-30 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e89b184-973c-36af-bf81-e97ee34d06df | -2.2435 | -53.72414 | 2024-10-30 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aa23165f-bcf7-34c7-a5d3-5c4076172fab | -3.66764 | -54.31139 | 2024-10-30 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d59dfdd4-e307-3734-92f2-0464a59888ff | -3.66253 | -54.30677 | 2024-10-30 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bdb0615d-4226-3ea5-8231-999fd2a9a7b5 | -4.50588 | -55.45433 | 2024-10-30 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a73972b5-4617-35e8-b843-f60d3a56d610 | -4.50512 | -55.4588 | 2024-10-30 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7990da20-8742-31d5-bd5e-f20e7abbc5fc | -4.26994 | -55.07539 | 2024-10-30 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09afb78f-97f8-388e-bd8c-142ed856ae46 | -4.14885 | -55.33051 | 2024-10-30 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8c255f02-5dd3-3192-a3a6-dce5013a808f | -4.14802 | -55.33527 | 2024-10-30 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c29c6c9e-84bb-3d95-8af9-30d185effe2a | -4.14195 | -55.33418 | 2024-10-30 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 17aea911-50af-3eb0-af4e-6aae08aa0e8c | -4.10445 | -53.94947 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 05f4870b-f706-3296-8084-58bc97925fa3 | -4.10381 | -53.95327 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f083255c-9394-391c-921a-db548bbc05b1 | -4.01952 | -54.80159 | 2024-10-30 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c38c093-a039-3cd1-b22c-afe07a3b25c9 | -4.01875 | -54.80603 | 2024-10-30 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89d0abad-147b-35a3-a198-aae9e7213dcd | -3.96881 | -54.14996 | 2024-10-30 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2a5933e5-c718-30e0-b53a-3764c02b7b62 | -3.96627 | -54.1489 | 2024-10-30 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f738dca3-b23a-3d20-a91a-f998dca6c519 | -3.95322 | -54.00256 | 2024-10-30 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 466b58df-1c1f-32d8-98ca-0ab243a8ef8c | 1.60192 | -55.62685 | 2024-10-30 04:19:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b98db866-dd6c-347e-a422-3f8b182bb33b | 1.5952 | -55.62797 | 2024-10-30 04:19:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28d57a49-461e-3993-9a8a-eb6dc67c8c31 | -1.63686 | -55.20647 | 2024-10-30 04:19:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c859e06-416b-3cbb-bf6e-b509a4e86bd0 | -1.59211 | -55.88919 | 2024-10-30 04:19:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16e82cf3-20e2-3d33-839d-ac1f4f274377 | -1.63458 | -55.20591 | 2024-10-30 04:19:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cfd840b-5d24-330f-bb86-d5173ad538c9 | -1.29937 | -55.72259 | 2024-10-30 04:19:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1bf35544-742a-3a31-9aae-65ad56d7f5d1 | -1.29758 | -55.73349 | 2024-10-30 04:19:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e3daa865-58a9-3d82-a2e7-d3fad4040df2 | -1.29108 | -55.7324 | 2024-10-30 04:19:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ba74420d-be28-3de0-b799-37c6f0b44b97 | -3.95574 | -56.05103 | 2024-10-30 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68cfd01a-6ff9-35fb-a250-da7a9ae441f3 | -3.9548 | -56.05648 | 2024-10-30 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96dd38fb-8db9-3278-9510-ad1f85014a91 | -3.93211 | -55.79025 | 2024-10-30 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 10dcdf62-3fc4-3d1d-9433-724a0a41f842 | -3.92969 | -55.78893 | 2024-10-30 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0be226c6-4065-3242-9195-d323e58331b7 | -2.72993 | -57.47881 | 2024-10-30 04:19:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| db65eb2b-3579-3fa0-bfb9-5e5294e167dd | -2.72876 | -57.48563 | 2024-10-30 04:19:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 73ed2f2e-bb30-3a2d-9dfe-b89e00f58e87 | -2.72287 | -57.47764 | 2024-10-30 04:19:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 18b1e34a-ac5d-3ef4-b7d3-077d8a2c5eed | -11.14282 | -37.42665 | 2024-10-30 04:21:00 | NOAA-21 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7cda639a-c92f-3d57-a258-83dfb63480cb | -11.14246 | -37.4269 | 2024-10-30 04:21:00 | NOAA-21 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b6237e41-7502-3cee-a8f5-aec638f6e52d | -11.14245 | -37.42958 | 2024-10-30 04:21:00 | NOAA-21 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f8788267-6aea-3d61-859b-34b0ea84a9ed | -11.14207 | -37.42981 | 2024-10-30 04:21:00 | NOAA-21 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cfa6898b-cad3-3f3a-b680-5809ea68ca44 | -13.78668 | -40.3282 | 2024-10-30 04:21:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5fc39c50-759e-3112-acd8-bb8eea31589c | -9.13757 | -40.92159 | 2024-10-30 04:21:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |


[Clique aqui para ver as próximas entradas](README48.md)
