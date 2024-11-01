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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9078ec38-ef94-395d-88e0-6f3a32787ba5 | -1.60018 | -52.38548 | 2024-11-01 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9ef76e0b-bf0e-3392-a153-ff77f9ce68a8 | -1.58662 | -52.1393 | 2024-11-01 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 113c3165-d59b-37c6-ae6b-a98642fe8cfd | -1.5858 | -52.14439 | 2024-11-01 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4d98c5d-3073-3dfe-a72f-0c6e07251a5e | -1.58276 | -52.1351 | 2024-11-01 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b0c2417d-3ac3-3ffc-b0b3-3e6a9ed356be | -1.5819 | -52.14019 | 2024-11-01 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 193f7240-dc9e-3670-9599-e5cdf2874575 | -1.58109 | -52.13306 | 2024-11-01 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 84a41ae5-5dc4-311c-babe-9eff86bfcb0c | -1.58026 | -52.13815 | 2024-11-01 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8a494aeb-5bce-3e11-9f62-9256302741d1 | -1.57943 | -52.14329 | 2024-11-01 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d45d7bfa-d22f-31ab-8432-974c7401ba80 | -1.43046 | -52.20577 | 2024-11-01 04:06:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 67f4b4d6-ff0d-315f-b755-7adaa5957e6c | -1.42491 | -52.19946 | 2024-11-01 04:06:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c7a94a9-a252-36ba-af4f-bdba3a3c5ddf | -1.42405 | -52.20469 | 2024-11-01 04:06:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1cbf951a-3d8e-32bf-b153-414a32b78b88 | -1.41765 | -52.2036 | 2024-11-01 04:06:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5377220d-4b51-38da-a406-ab2d2764b611 | -1.41679 | -52.20883 | 2024-11-01 04:06:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 147451db-9e71-3e99-9a6f-33dcd6d93b05 | -3.2554 | -53.07503 | 2024-11-01 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1e591bb-e2ba-321c-a4c9-8be160b4f5e5 | -3.24879 | -53.07408 | 2024-11-01 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c8baaf8-a260-397f-b939-82bc27d3e65a | -3.23894 | -53.36637 | 2024-11-01 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| edd91124-b5ab-3c04-8cac-93ce1282b583 | -3.2379 | -53.37243 | 2024-11-01 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 4c43dbd2-fe5a-33aa-ab2e-4a5dbdd7d7a6 | -3.23229 | -53.36499 | 2024-11-01 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 16253942-4de9-3a1a-9e9a-41b7bae63221 | -3.23124 | -53.37104 | 2024-11-01 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 703cd276-ab68-3c00-81e4-58a1bdb3eb74 | -2.24075 | -52.77003 | 2024-11-01 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2d823e9-51a4-3922-8051-beebb25bea35 | -2.23423 | -52.7687 | 2024-11-01 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef628e05-77ab-3cd1-88f5-3ac2084efbe9 | -2.88179 | -52.89431 | 2024-11-01 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 635b030b-5f94-3aff-a743-1bfe15f3d6e7 | -2.87775 | -52.88857 | 2024-11-01 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f9c91e04-0875-3c6c-a4e6-81f60f0fa253 | -2.87688 | -52.89384 | 2024-11-01 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9aac9e20-f570-3989-9596-1f7c03e24ded | -2.87614 | -52.88806 | 2024-11-01 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 52d168e9-252e-37ea-b5e4-040aedaf825b | -2.87522 | -52.89338 | 2024-11-01 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cb09e19d-63bb-3c33-89ca-849cf3b996e6 | -2.87429 | -52.89879 | 2024-11-01 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8171a611-2af1-3b9c-b260-4a672c60ede4 | -2.87032 | -52.89279 | 2024-11-01 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7ae23fb7-018c-3650-a67d-6d273f667229 | -2.86867 | -52.89233 | 2024-11-01 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cc00a749-542d-3e90-bb30-4dd740934130 | -2.16211 | -53.67481 | 2024-11-01 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a872dce0-28b0-3798-bfa1-69967705f0c7 | -2.16197 | -53.67179 | 2024-11-01 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8ce9325a-9c3a-3d4c-9bf9-575e600154dc | -2.16102 | -53.68135 | 2024-11-01 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 34228b1a-3bdc-3656-a044-599e525e5b96 | -2.16083 | -53.67836 | 2024-11-01 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f74240c0-3d17-3f1f-b6ec-000769ca3d35 | -1.17431 | -53.67831 | 2024-11-01 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24521b44-6755-34b4-8d7c-8613813a9c88 | -1.17333 | -53.68423 | 2024-11-01 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4945392-f249-3fcf-b935-663ebf61fdfd | -1.16641 | -53.68245 | 2024-11-01 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5b7a70d-a23e-3eff-a685-f7b5201e9e0c | -3.05176 | -54.1729 | 2024-11-01 04:06:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 79558bc3-45ec-39df-9018-5fb52a034dd3 | -3.04472 | -54.17173 | 2024-11-01 04:06:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 46100f4e-131e-3086-86cb-7dc46aa59760 | -2.47857 | -53.98177 | 2024-11-01 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb027758-126b-3124-ab0e-6c993f3e4fe4 | -2.4774 | -53.98884 | 2024-11-01 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 44ec4582-103e-3c89-b709-a721cd83f8d2 | -2.47492 | -53.98675 | 2024-11-01 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d469ff82-a42f-3a35-a352-091eff1ba48b | -2.47372 | -53.99369 | 2024-11-01 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| affa395d-e8ea-3ce2-9e0f-7862c6c1b585 | -2.47043 | -53.98738 | 2024-11-01 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 17ff67f3-de38-3c25-9368-79b091d55870 | -2.46794 | -53.98534 | 2024-11-01 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ddd2f3d5-317b-3a4f-96bd-ca06717bf58a | -2.96844 | -53.91194 | 2024-11-01 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 820c32d3-f73d-3c50-8df3-c47023076b97 | -2.96152 | -53.9106 | 2024-11-01 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f43c64cc-fa0a-3625-b64f-0aabeb9fee90 | -2.92021 | -54.19486 | 2024-11-01 04:06:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d7ca87dd-9167-3d77-9ae7-7cd291ba7ee2 | -2.91805 | -54.19131 | 2024-11-01 04:06:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a4432d8e-8388-354d-b6a0-674eaeb42763 | -2.91686 | -54.19806 | 2024-11-01 04:06:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d0adbde6-4fb2-3401-a46e-e113032ab873 | -9.9187 | -64.8058 | 2024-11-01 04:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.6 |
| d7d975cc-5146-31f7-bd23-fd47c8c125e4 | -16.9204 | -57.5291 | 2024-11-01 04:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.8 |
| 5c233b87-b82b-3985-ac48-896fbfab5931 | -9.6353 | -40.58141 | 2024-11-01 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| b53c220f-8b0c-3fab-8fff-e4fadddc7510 | -9.6387 | -40.58194 | 2024-11-01 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 14ba26c9-3d6f-300a-8048-e4d9214e6bb5 | -9.63814 | -40.5856 | 2024-11-01 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| cbf01ad8-8794-394e-9ee7-f8333d59b96c | -11.34136 | -38.79467 | 2024-11-01 04:08:00 | NPP-375D | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f64ec3f4-deaa-3e8f-ab52-080b2c0a4eb7 | -12.23907 | -40.97504 | 2024-11-01 04:08:00 | NPP-375D | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0c564011-2a7b-3a8b-9ce2-276651d260ac | -11.94378 | -41.6283 | 2024-11-01 04:08:00 | NPP-375D | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 624c70bc-6246-353f-b97d-741d156aa481 | -11.94042 | -41.62776 | 2024-11-01 04:08:00 | NPP-375D | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5c12b5c1-ea90-3523-a2a1-4ce296aa9c16 | -11.80282 | -41.23519 | 2024-11-01 04:08:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6de6a5c5-575e-3806-b415-6d651c247517 | -11.53948 | -40.41292 | 2024-11-01 04:08:00 | NPP-375D | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1d1854d8-da38-3548-a73e-6acafeec9a5e | -11.50547 | -40.4748 | 2024-11-01 04:08:00 | NPP-375D | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5bc49ff7-a420-3931-9aae-83a3df254845 | -11.28671 | -40.95683 | 2024-11-01 04:08:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5905c209-f345-38de-990c-548b5fb5edd3 | -12.62213 | -41.18501 | 2024-11-01 04:08:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 61439bda-6df6-3388-b1fd-c35b81927442 | -12.49671 | -40.86342 | 2024-11-01 04:08:00 | NPP-375D | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a7d541ef-bc64-3b79-9729-9724581a9e5f | -12.02143 | -42.14841 | 2024-11-01 04:08:00 | NPP-375D | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 4ef07289-c46c-3441-a931-37400600b83f | -11.49934 | -43.22903 | 2024-11-01 04:08:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| be886ccd-ca72-3fea-ac1c-521f1e4475fa | -9.41408 | -45.76229 | 2024-11-01 04:08:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a401155-eecc-3f04-80f9-fca7ade829e6 | -9.85093 | -36.49279 | 2024-11-01 04:08:00 | NPP-375D | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 96f0b4ec-3753-3462-932e-934f5d7c371b | -9.84984 | -36.5006 | 2024-11-01 04:08:00 | NPP-375D | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6b54f98d-4e79-3c84-a787-2be4fe126d7a | -9.84616 | -36.49607 | 2024-11-01 04:08:00 | NPP-375D | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 35bfef3e-f202-384e-ad9a-daa1efc34209 | -9.8456 | -36.50004 | 2024-11-01 04:08:00 | NPP-375D | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| becefb01-9555-3226-81f4-2d5fe0cad56d | -9.84505 | -36.50402 | 2024-11-01 04:08:00 | NPP-375D | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| db866f62-9109-3485-a672-037581499b30 | -9.84247 | -36.49158 | 2024-11-01 04:08:00 | NPP-375D | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f56d861a-d98f-3d1f-9057-53e200b89b19 | -9.84193 | -36.49549 | 2024-11-01 04:08:00 | NPP-375D | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f9366671-fefb-3cb2-99f1-1bfce48106aa | -9.84137 | -36.49946 | 2024-11-01 04:08:00 | NPP-375D | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9b246432-b0d5-39ec-8f9a-2a5d9aabca58 | -10.28678 | -36.31982 | 2024-11-01 04:08:00 | NPP-375D | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e7e73368-7427-378f-acf8-65ef65bbb382 | -9.3862 | -40.33998 | 2024-11-01 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a83a73de-c53b-3b48-a946-2d61d50bf00f | -8.81518 | -40.17537 | 2024-11-01 04:08:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 276b8b69-f596-39b5-8178-189e8f68ec31 | -8.68973 | -39.63035 | 2024-11-01 04:08:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 703221a1-6262-392c-a7a2-f0c6dd66c966 | -8.67735 | -40.20779 | 2024-11-01 04:08:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1a42b89f-d99f-352d-85c2-fab54d50776b | -9.38279 | -40.33945 | 2024-11-01 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 87f38e8e-5e9a-339d-ab15-757ece164f42 | -8.81575 | -40.17165 | 2024-11-01 04:08:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2708dcf1-68bb-32d0-b094-06f393cd1cc0 | -9.63475 | -40.58507 | 2024-11-01 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 823817dc-0d39-3809-aa30-94e9e5843cea | -8.50667 | -40.93646 | 2024-11-01 04:08:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 06fb277c-85a6-3088-a729-2e97d254bb11 | -8.50612 | -40.94002 | 2024-11-01 04:08:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 81cbdd7b-cba4-34a0-9356-03c0b0c7ea82 | -9.82858 | -41.79257 | 2024-11-01 04:08:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2e418c71-095b-388f-8371-f423b568348b | -10.98765 | -45.11179 | 2024-11-01 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2cea562c-77fb-3fb9-a5d8-92022010ed87 | -10.98697 | -45.1158 | 2024-11-01 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bfa5b0a8-6080-3328-9678-2a22aa9412a4 | -10.9863 | -45.1198 | 2024-11-01 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ac680464-669b-30f5-9a05-1abe398ada69 | -10.98412 | -45.1112 | 2024-11-01 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e7b86245-5e8b-30f4-bcbd-35a2e20cff7f | -10.98344 | -45.11521 | 2024-11-01 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f959e43b-681e-354b-ad68-af0e798b377f | -10.98277 | -45.11922 | 2024-11-01 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 86d53528-8780-35a9-8007-219d1438956b | -10.9821 | -45.12322 | 2024-11-01 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8454f74e-5c53-38e0-bb86-28e8889f5808 | -10.97857 | -45.12263 | 2024-11-01 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4f390d2a-f27e-3682-b678-1377fcf5bd69 | -10.9779 | -45.12663 | 2024-11-01 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73f31cd3-4b7a-32ce-acca-2ed3e29074c8 | -10.55688 | -51.92415 | 2024-11-01 04:08:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2543dece-1b3b-3c58-93b1-ff6ae61ce88e | -10.5562 | -51.92775 | 2024-11-01 04:08:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 232751eb-e144-3741-be18-581b8c12f127 | -16.91466 | -57.52892 | 2024-11-01 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 5d94b5e3-4ab3-3456-9a11-b0c750c6ceea | -16.91405 | -57.53 | 2024-11-01 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 365ecfd5-34cd-3e5e-9b63-04e1b1bc8950 | -16.90939 | -57.52087 | 2024-11-01 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |


[Clique aqui para ver as próximas entradas](README24.md)
