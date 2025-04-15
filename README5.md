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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 371e6690-a079-35ca-b860-645bb135df44 | 2.39333 | -61.28269 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81c26f95-9a72-336b-b793-68c8ce5c817f | 2.40554 | -61.29515 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 93073e58-ba6a-39fd-ba62-68b44ddcf861 | 2.40781 | -61.28767 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ec0c54c-19c2-3347-bb32-c42539d0552c | 2.80142 | -60.05855 | 2025-04-15 05:25:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42ced82e-d2b2-33fe-b07d-f720aca7ac7e | 2.39668 | -61.28218 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4539824d-e936-3b79-9506-4348f8843727 | 2.40392 | -61.28468 | 2025-04-15 05:25:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ac3ec08-8511-3cd2-bef1-287024edebe8 | -2.95676 | -60.01577 | 2025-04-15 05:27:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af6af9cc-c9fb-318b-9b14-6616e1bec581 | 2.3965 | -61.2859 | 2025-04-15 05:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 44.8 |
| e7242cbb-ef3c-35da-845b-423a7693ec27 | 2.3964 | -61.3048 | 2025-04-15 05:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 2bb25c8e-4f03-3578-a5fa-a2591b82c7e1 | -14.62825 | -59.9998 | 2025-04-15 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10b9a67f-8412-3647-a86d-654aaee689a7 | -16.21292 | -58.09514 | 2025-04-15 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ec20edc2-c9ed-36d8-8124-b98d8b931692 | -6.36238 | -43.64619 | 2025-04-15 05:36:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 3c9720cf-4dd3-3d24-9a95-c17c0272d09f | -6.35308 | -43.64475 | 2025-04-15 05:36:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 60dcb9fc-0325-35da-a96f-57d49e3c95a2 | -6.35159 | -43.65492 | 2025-04-15 05:36:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 0be2e234-8c1e-3b8f-89b9-b3ffeab981de | -5.56688 | -44.52985 | 2025-04-15 05:36:00 | AQUA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a6567c23-7f77-3060-8b29-bef544f52a2d | -6.36091 | -43.65625 | 2025-04-15 05:36:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 19d2ff9b-f7a5-34c2-8718-ce3b2a068332 | 2.3964 | -61.3048 | 2025-04-15 05:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 35.1 |
| ddfa0a9e-acc2-3d0b-9f7c-444e6a5e8e6d | 2.40707 | -61.28839 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ec489f6-d50d-38bb-bcbc-6b57e6e51281 | 2.40421 | -61.2965 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 528116b0-40be-3f3b-a5a0-249a6ef9d658 | 2.39584 | -61.29318 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3a65c593-244f-3d8c-8668-92c67beeda7a | 2.39659 | -61.30104 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd922e7f-f98d-3fec-b87f-90846855ad42 | 2.39949 | -61.29324 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ab817e08-b745-3655-a83c-abe1a1db060f | 1.64948 | -60.23046 | 2025-04-15 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 336b38c6-4e6f-344d-9e8d-8e3a1fe130a2 | 2.39071 | -61.29076 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bf7252e-014b-379b-90b2-a5cc787b10f7 | 2.39479 | -61.29014 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed90b446-1936-3676-b67e-48c6b8816ccf | 2.40297 | -61.28895 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc2aeced-9dd1-3598-afaa-09ca462d88fe | 2.39828 | -61.28589 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f8e3114-803d-3fd7-b147-786748bd2596 | 2.40359 | -61.29271 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 03125c85-427a-3613-9235-a26635fd0ec1 | 2.80187 | -60.05609 | 2025-04-15 05:53:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2652c711-b832-351e-9764-9dec8200b8a0 | 2.3947 | -61.28593 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53230b2a-fb71-35c5-be9c-1982dde9933b | 2.39527 | -61.28957 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ad7dd59-0200-3c6c-9f6f-543d3c438145 | 2.40771 | -61.29231 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03d81c1a-2e31-3919-bd03-a778f7a019cb | 2.4007 | -61.30056 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3a162fcd-e121-3609-a383-1bf816e66918 | 2.39233 | -61.29742 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d890243d-e3c3-32d0-96d0-b84b7f92b273 | 2.3929 | -61.30104 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ebd3ca10-e29d-3d78-993f-510c2fac494c | 2.39419 | -61.28652 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f470b37-f04b-3c82-bb79-cb39cf904d94 | 2.80256 | -60.06039 | 2025-04-15 05:53:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ca71ab4-d628-3cb3-85e2-7160a50ec3fe | 2.39699 | -61.30047 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e984b00-a95b-30e7-a7f4-a286c2926f62 | 2.39888 | -61.28954 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2bc9ff07-28c7-3e8c-9aff-778547373660 | 2.40644 | -61.28462 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6161ca65-74a3-3da8-a292-59b136da325f | 2.3919 | -61.29799 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 16d35ffc-daf4-3a86-b86f-7e13b6e4cd20 | 2.3913 | -61.29437 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fef0da7d-a1d5-3d83-89c2-b1d59ffc2528 | 1.65018 | -60.2348 | 2025-04-15 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90284bba-3361-3e44-b0e9-a74280043709 | 2.39176 | -61.29381 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 624befc2-611f-3517-9f0e-9350c4e148dd | 2.39641 | -61.29681 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 67fc8244-56e4-3593-82cc-78e499f4ffce | 2.4001 | -61.29692 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e3aab27a-11c5-3757-8fc5-38e0e9f9a29b | 2.39118 | -61.29019 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05c351ed-213c-3838-983d-962cd089512b | 2.39539 | -61.29375 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 81938e50-0f9c-3595-ab9c-7b1d1925f54d | 2.40236 | -61.28522 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1660746f-7c95-32ba-b67c-11b89875aa35 | 1.64879 | -60.22609 | 2025-04-15 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28a61135-9196-3cc0-96ba-22ac5947f21f | 2.39599 | -61.29737 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7815c33a-5797-3155-90b4-61385f8b8455 | 2.3925 | -61.3016 | 2025-04-15 05:53:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d789cb83-a865-3daa-9428-46fce5decb10 | -4.28831 | -62.67114 | 2025-04-15 06:16:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4299b68b-1ff6-3466-a9ed-82876b20f8f2 | -3.91825 | -62.50951 | 2025-04-15 06:16:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65c30978-9060-3532-b50f-ae4d44f21b63 | 2.39687 | -61.29687 | 2025-04-15 06:16:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 8c6860a3-c3da-32c6-8370-325c6f38303a | -4.71363 | -64.73148 | 2025-04-15 06:18:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 753efde8-b921-3fc9-8975-fe265216f71a | -4.11016 | -38.18028 | 2025-04-15 12:12:00 | TERRA_M-T | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 11626a93-222d-3f69-b429-cc3709c7663d | -5.64818 | -43.70744 | 2025-04-15 12:12:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| b38dc537-8a84-35bc-8873-463963cab55a | -10.56402 | -38.76677 | 2025-04-15 12:14:00 | TERRA_M-T | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 90d28e30-aab2-309c-b17c-c2f97a59e1c6 | -11.98109 | -41.32376 | 2025-04-15 12:14:00 | TERRA_M-T | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| f233eddc-8094-3c32-bc72-72d19ec9f307 | -10.62983 | -40.20739 | 2025-04-15 12:14:00 | TERRA_M-T | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 107.3 |
| 95934d65-c17f-36ee-9cd7-be5b51140f78 | -9.82365 | -36.98494 | 2025-04-15 12:14:00 | TERRA_M-T | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 2077aed5-69c8-3a2f-86e1-8442a647fb51 | -8.48301 | -44.39183 | 2025-04-15 12:14:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 798cce75-a00b-332d-b181-b81e12fa13da | -10.66223 | -40.11668 | 2025-04-15 12:14:00 | TERRA_M-T | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 2dbe5b3b-e263-3e59-a199-e37c59515381 | -10.63138 | -40.19567 | 2025-04-15 12:14:00 | TERRA_M-T | ANTÔNIO GONÇALVES | BAHIA | Brasil | 2901809 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 22c4d47a-07ba-3991-92ee-5991ffda3c3c | -8.94156 | -44.2258 | 2025-04-15 12:14:00 | TERRA_M-T | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 81ccd655-86fa-317b-b6e6-721acae1daa8 | -8.68962 | -44.36787 | 2025-04-15 12:14:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9047f88f-697d-317c-8dea-9fcbe6148f48 | -9.82135 | -37.00391 | 2025-04-15 12:14:00 | TERRA_M-T | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 4957bc92-4e3d-390b-9b59-2062f5e41241 | -13.5419 | -39.77356 | 2025-04-15 12:14:00 | TERRA_M-T | WENCESLAU GUIMARÃES | BAHIA | Brasil | 2933505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 900c48b0-8443-30d7-ae79-3a795e7e1bd7 | -9.8204 | -36.99815 | 2025-04-15 12:14:00 | TERRA_M-T | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 44.3 |
| b079c114-98ad-3225-bce8-3d888a9f1017 | -17.901 | -44.40095 | 2025-04-15 12:17:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1971cad9-5005-3041-bd2c-80d674a5c18b | -17.90987 | -44.40231 | 2025-04-15 12:17:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 44864f2a-5a91-36c0-8cf0-2d08b25ff53f | -17.89969 | -44.41023 | 2025-04-15 12:17:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 746b13f6-439b-39bd-96e0-6dbb0aefe8b9 | -18.97568 | -41.69215 | 2025-04-15 12:17:00 | TERRA_M-T | TUMIRITINGA | MINAS GERAIS | Brasil | 3169505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 6a6fced1-ed29-3fcb-bc89-92cc486fb61b | -19.95779 | -45.30302 | 2025-04-15 12:17:00 | TERRA_M-T | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 71c18d0a-bf8a-3624-84ab-0f33cb93d3c0 | -21.47517 | -47.14845 | 2025-04-15 12:17:00 | TERRA_M-T | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 970a2e0c-e2d7-3d3d-a879-665f9624936c | -29.79482 | -51.52384 | 2025-04-15 12:19:00 | TERRA_M-T | TRIUNFO | RIO GRANDE DO SUL | Brasil | 4322004 | 43 | 33 | nan | nan | nan | Pampa | 11.7 |
| 28ffacf0-36fc-30ff-befe-ae999118cd0f | -10.6267 | -40.2106 | 2025-04-15 13:50:00 | GOES-19 | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 81.9 |
| 99109cb4-6fd0-3807-a306-960eb06d5928 | -10.6267 | -40.2106 | 2025-04-15 14:00:00 | GOES-19 | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 85.5 |
| 6734831a-5c86-344b-a1d7-d60312c3e066 | -10.6267 | -40.2106 | 2025-04-15 14:10:00 | GOES-19 | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 123.2 |


