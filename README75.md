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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0af5c687-22d9-346a-8e14-3acb6a1588f1 | -8.55689 | -64.04008 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1eaad8f7-0393-3f67-8551-4cf710765496 | -8.10806 | -63.69577 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e84f15be-c831-3f7c-9668-55e341e2ad60 | -8.04233 | -63.87239 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 557e8228-93d6-316a-89b7-f70503cd8dc5 | -7.95312 | -63.63049 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3dc2fe2-868f-356e-8e7a-36fed252c0e6 | -7.95255 | -63.63423 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ff4c2a6-3f9d-3467-ad0d-9eb097b69be0 | -7.95026 | -63.62621 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36b96d57-d16e-317b-b615-70a749810ea2 | -7.94969 | -63.62997 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f5c2bb0-23e1-3740-8d8d-77b350ae454a | -7.94912 | -63.63371 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4c2ea52-e686-3dda-8437-556f54f8dfef | -7.94684 | -63.62568 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9fb8a21-9ea5-3a8b-8a62-30b4e1ea0efa | -7.94627 | -63.62943 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aedf3cb2-e604-3510-8868-0ee92846b926 | -7.9457 | -63.63318 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5be8f7e6-63f5-373c-93cf-1848927db38d | -7.94284 | -63.62891 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb86ed99-1449-34fe-9e33-b9d86b3cb59e | -7.94227 | -63.63265 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4466f7ac-dbaa-3125-8198-0df6cc718784 | -7.90897 | -63.50431 | 2024-10-15 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 724bdac7-e973-37f7-a5f9-fc077bacebe4 | -8.80712 | -63.18146 | 2024-10-15 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a85b960-21ad-35d1-8556-75b4b6cd9b1a | -10.26532 | -63.10827 | 2024-10-15 05:44:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a26e500b-fec1-3b93-a2e1-4af4dce1faaf | -10.26174 | -63.10771 | 2024-10-15 05:44:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 22b95abf-3fcf-3b9e-a78e-47285351b1a0 | -10.25815 | -63.10719 | 2024-10-15 05:44:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 473497f5-74c1-36e2-8c63-bef158ec0bc6 | -10.25457 | -63.10666 | 2024-10-15 05:44:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 788c312b-5267-303d-97ba-ffe9cae66545 | -9.77843 | -63.15025 | 2024-10-15 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a03180f1-b4ed-3c2f-afa3-104b69cbf529 | -12.058 | -64.67838 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8d24233-36d0-3956-bd22-e735c82a65cd | -12.05743 | -64.68214 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebb224c4-ef69-3535-90e3-7eece6f3e6fc | -12.02393 | -64.71916 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6eee6ec7-123c-30e7-aa67-697bc27f2031 | -12.02052 | -64.71863 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0324823e-8ae9-34e8-87b8-ea9af5aea28e | -11.96217 | -64.75932 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74bfb774-dbe7-3bfd-9f62-16515c79dc52 | -11.95821 | -64.76254 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa2c84a2-1b9b-3465-a681-7092fa9d3668 | -11.95766 | -64.76627 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18b4a2d7-e000-3ee1-9fff-c122b7c22647 | -11.94996 | -64.84122 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76507055-7e0f-3924-9f33-57c350aef7b9 | -12.50868 | -63.96896 | 2024-10-15 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49b0dc20-049e-3e22-8e7b-1efe73914098 | -12.50516 | -63.96841 | 2024-10-15 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc27e496-20f3-3349-b571-3dfb9f8616f0 | -12.49808 | -63.94 | 2024-10-15 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c70e06d8-8076-3804-baea-b1497dc65e95 | -12.49748 | -63.94404 | 2024-10-15 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 619a8360-6497-364c-953a-3f23939e9964 | -12.49336 | -63.94754 | 2024-10-15 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e75d77ef-0ad9-3245-987c-35883261fdf5 | -12.49036 | -63.96771 | 2024-10-15 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c8b2642f-4917-38ee-953e-8e5f5aacb468 | -12.48923 | -63.95105 | 2024-10-15 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 52851bd0-b412-3366-a3de-06acf155f3ef | -12.48684 | -63.96718 | 2024-10-15 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7b497db-0e59-3770-b051-27aa89fd6abf | -12.48511 | -63.95454 | 2024-10-15 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a238c71-8455-3600-b32c-edf04d57ae19 | -12.48391 | -63.96261 | 2024-10-15 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0dc9f353-b3cd-3b71-9f5b-a91bdabe2f55 | -12.39418 | -63.71289 | 2024-10-15 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 14022e6e-2667-3819-90fc-05aa533dfa20 | -12.39297 | -63.72112 | 2024-10-15 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a27c9ad0-1b1c-3d32-a33f-bf057b3e4677 | -12.39001 | -63.71647 | 2024-10-15 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 65356aae-4707-314e-8194-083225c2c480 | -12.38941 | -63.7206 | 2024-10-15 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 48cf642b-a7db-3108-b117-66cbceac265a | -12.38881 | -63.72471 | 2024-10-15 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3aa0faf9-521b-3efe-b880-c85fd7ee8496 | -12.38821 | -63.72881 | 2024-10-15 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f525750e-82b0-3d2f-8e9a-5c8e169ff200 | -12.38645 | -63.71593 | 2024-10-15 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2b36898-de1f-3183-a1dc-403a71facc5e | -12.38585 | -63.72005 | 2024-10-15 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49b3b008-470c-37f3-b5d9-3d495394df42 | -12.38525 | -63.72417 | 2024-10-15 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34c9e54a-c51e-364b-8fb6-e970a9832afd | -12.38465 | -63.72828 | 2024-10-15 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d7110144-46d5-3c61-af41-1bbe032c10b6 | -12.35274 | -64.31981 | 2024-10-15 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b54abf2a-e9fe-3a7e-a528-4456d84b2bf2 | -7.46545 | -64.15286 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9597e7d-6ec6-3680-8aec-8698f2947a3d | -7.46303 | -64.25095 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b672b2db-ef99-3f71-97e3-3251ab6ff524 | -6.67364 | -64.60874 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a7321e6-c3f4-3148-a2fa-b3abd1946126 | -9.4401 | -64.5737 | 2024-10-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 72fe9cd9-4328-357e-badb-83d4da2578e5 | -8.73119 | -64.23148 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c35af14-a4f1-3727-83a4-bbf553e2b91b | -8.73063 | -64.23513 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20810dda-4fc9-30cf-b677-49bd1c16756c | -8.73007 | -64.23877 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 71108e5d-eabc-346c-b6f2-8661bfda789f | -8.64909 | -64.12574 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fcecee6e-63e6-3f9a-9fbd-ff57d0c57226 | -8.60019 | -64.21911 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d097a91-2ed4-3443-967e-82372c1b2660 | -8.59681 | -64.21858 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a40eea1-aab7-3c60-b407-a8614c4a8d96 | -8.59626 | -64.22222 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b9fedd8-c36c-382e-bc62-606341ec7edd | -8.59344 | -64.21806 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 805ddc6b-d9a0-355e-a559-9665e6e6a22f | -8.59288 | -64.22169 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f0170b0-eca2-3b0a-96a6-b5886ee07f73 | -8.17733 | -64.11702 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ef116e6-e366-36c3-a310-451fcc3ad294 | -9.09996 | -65.27976 | 2024-10-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 01da674e-15e5-326d-998c-b197128e7483 | -9.09942 | -65.28326 | 2024-10-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4e1fd255-63ea-3ab5-8ef0-d8844ddfe08d | -9.09887 | -65.28676 | 2024-10-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf445e96-1743-3875-8d70-b2212750c7c1 | -9.09833 | -65.29025 | 2024-10-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0cdc897-e228-3b37-bec9-e5498d0892a2 | -9.09665 | -65.27924 | 2024-10-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b7b324db-712c-32a1-8d6f-63c59a7d6c24 | -9.0961 | -65.28275 | 2024-10-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 41cf2ab0-e56a-3676-a1bd-4c5f0c29fff4 | -9.09556 | -65.28624 | 2024-10-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b8d7e5c7-2a65-35ca-a8cd-5f24b94ae470 | -9.09502 | -65.28973 | 2024-10-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15e6c85f-d301-3ad8-a29d-f37450275965 | -9.09448 | -65.29324 | 2024-10-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d9432f9c-10d8-3779-812b-5eccd014c902 | -9.09333 | -65.27872 | 2024-10-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 82a53f83-66fb-3a87-beae-848df33843ac | -9.09279 | -65.28223 | 2024-10-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 980ad56c-e24a-393e-ba83-0faebe1ce241 | -9.09225 | -65.28572 | 2024-10-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7b085d7c-7519-3dd6-8d94-a8bfdd22ad2c | -9.09171 | -65.28922 | 2024-10-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8d74fde5-f14c-38dd-9236-d5538b9945d3 | -9.09002 | -65.27821 | 2024-10-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83e9987d-4905-3145-a22c-58b5e8a52ef7 | -9.08948 | -65.2817 | 2024-10-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2dd6f751-94d7-345d-8feb-45e2f24235d3 | -9.08894 | -65.28519 | 2024-10-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f91455c1-9e24-3977-ab03-2a69c3252c7c | -9.0884 | -65.28869 | 2024-10-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a0a8803b-8667-3399-913c-816bfdd75986 | -9.08671 | -65.27768 | 2024-10-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3419289f-ad6a-3959-bd28-f6b523389d68 | -9.08617 | -65.28118 | 2024-10-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6eb7b4f8-c77a-3601-805a-f6ed61ad8ff7 | -9.08563 | -65.28468 | 2024-10-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 776a1940-4f54-3166-8d5c-d940cc843e02 | -9.08508 | -65.28817 | 2024-10-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96419531-b825-34f1-8f37-6fe1f3e5058b | -9.08286 | -65.28066 | 2024-10-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 114779b3-cd7a-31a7-9774-9b22d8fafdb7 | -11.93031 | -64.87992 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ba2e812-3b0d-3577-a32a-911bd8be40dc | -11.92898 | -64.8804 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e10fd977-580a-3cde-aa03-2c1f757ff1a3 | -11.9256 | -64.87987 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1669c505-639e-3cef-95a7-b3db62c4e752 | -11.92221 | -64.87935 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6498067d-81e2-3fbf-90f1-bca5c0359b68 | -11.91882 | -64.87881 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37021e49-e6ce-3dca-bfef-26a8ad5a3638 | -11.81326 | -64.83576 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a23de6e5-f2a9-3048-953a-7b3e64f30f2a | -11.8127 | -64.83945 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ae05d41-fcab-3ef1-84c4-b449d67bef64 | -11.80987 | -64.83524 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 736d4cf2-5755-336f-9b2c-34d4018e51bd | -11.6977 | -65.23312 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 693659d5-db99-3318-b9f9-c18861b06f9f | -11.69715 | -65.23672 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c2195de0-4dca-3b15-b1df-f7ac43502b58 | -11.6949 | -65.22897 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 423a291c-dcf4-3c60-9d0f-c3dc77251648 | -11.69435 | -65.23259 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 741fb05f-1d8e-3f14-8f23-4bf93230c2eb | -11.6938 | -65.23621 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ed400c79-fd1b-32b0-9abe-16e3fca182b2 | -11.69325 | -65.23981 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fe6d8928-6b7b-3ba2-bf6c-5bf0a18031ca | -11.69155 | -65.22845 | 2024-10-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |


[Clique aqui para ver as próximas entradas](README76.md)
