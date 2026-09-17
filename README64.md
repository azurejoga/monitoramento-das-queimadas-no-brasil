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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b638a5fd-a089-3b06-8f0c-8481d2d62d3e | -5.85888 | -51.94381 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6123801-daac-3ec6-a25e-7e00dc82e4c6 | -5.83779 | -52.03179 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0744d48-1c4c-33f6-9113-f8f2cd959ea5 | -5.88766 | -52.08664 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cc80e16-8da4-3b3c-8511-7a76fafb51ee | -5.36004 | -56.04471 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d96de35d-168d-3605-b99a-36108d0fabd0 | -9.11445 | -45.73236 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 36.8 |
| c5c3e201-62ae-343c-aff3-94a56e6489e7 | -7.01473 | -43.37719 | 2026-09-17 05:16:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 14dc3d7d-97b3-31b5-95ea-2834d14474bf | -7.58739 | -46.33072 | 2026-09-17 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e3a54be-d91f-384c-ac3d-8d88113be17a | -6.70767 | -58.80055 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4cce7a5-de89-30bd-855d-b308afc42917 | -4.38026 | -55.03062 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1b87a89-f8e5-36e9-9d60-8f497dc8a2e4 | -6.83006 | -58.9844 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a42292ad-f451-3259-ac5e-b8f456e51e12 | -3.02217 | -51.33652 | 2026-09-17 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd56ea1a-0b79-3896-892f-ae1afe7d8fea | -3.1319 | -59.02453 | 2026-09-17 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| abea91b0-0b4d-3614-88a8-58529773f4cf | -3.44307 | -50.6583 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2395ab8c-e0e1-30f7-ad9c-4cb2eb49fa4f | -5.83617 | -52.11688 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fa47deb-7b55-3109-ad41-94d055ef04a3 | -8.57722 | -44.5834 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9f2340c4-500a-38b5-99cd-25164f4cfd71 | -5.14093 | -55.93172 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4fb3b6ce-ba07-380a-a101-ad884b962945 | -7.45432 | -46.16816 | 2026-09-17 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2070c9d5-d6fe-3f48-a499-4a473c7a2deb | -3.47654 | -54.69328 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e7b429c-a82a-3bb4-bb17-839655e44f35 | -3.82421 | -55.78336 | 2026-09-17 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5115d1a1-aafc-3cf4-82b1-f1ddee4e3e62 | -2.90755 | -54.18347 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee66213a-82d1-33c9-b037-31438033a47a | -3.33508 | -59.83162 | 2026-09-17 05:16:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 990cc067-3b96-345a-b220-3ca40ee6e147 | -6.70349 | -59.45853 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a0b65fdf-c5d8-389b-beb2-49c46a694113 | -5.80868 | -47.24371 | 2026-09-17 05:16:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 7d6c96a7-3a03-3075-81f2-944eb20b24e7 | -7.36898 | -44.47871 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e19b58f6-18f3-3522-a24c-79dab26d8ce3 | -2.84471 | -57.63633 | 2026-09-17 05:16:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e77fb807-a42c-323d-bd62-79ab6b35c310 | -7.83364 | -50.23305 | 2026-09-17 05:16:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80fccedb-6cd8-31d8-b11b-2be0f5aadfb1 | -10.11555 | -45.62838 | 2026-09-17 05:16:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 846140d8-345f-384f-b36a-5d8d5a20182c | -3.54174 | -55.47563 | 2026-09-17 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5cabd4b-ee5c-3fcd-9a03-1e144ec66885 | -9.12149 | -45.72435 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eeafebc9-51b4-3095-b9be-683fa0b723c8 | -4.51863 | -54.94928 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94724ba4-5878-3642-bf35-1dddf930ca12 | -2.78255 | -51.36644 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45ddd77c-00b5-32fd-b0e1-7e0b8a3dc340 | -5.63515 | -44.80439 | 2026-09-17 05:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9af0786a-dff4-33c9-b034-e21d6b522ced | -4.49149 | -55.50172 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4340cedf-6a82-3dc3-b02b-6f615b4e9302 | -9.11389 | -45.73687 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a11d4b80-4870-35b6-9481-9f0ee03e539c | -3.33589 | -59.82654 | 2026-09-17 05:16:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 28cfeaaa-1ff8-30a0-8801-0f124e858517 | -8.57849 | -44.57353 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fb3b3acf-2433-36f0-a69f-9c19161d4e2a | -8.39091 | -42.20349 | 2026-09-17 05:16:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 76606761-f579-31fb-97a2-1b06053fc63d | -4.47953 | -55.08873 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95803897-5dfd-315d-a147-33f7c76e22ba | -6.1402 | -57.69729 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7a8be8c-54f5-3cf8-8e91-a3b114595949 | -3.26115 | -54.27458 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8035476a-35c8-3895-9a58-5ce87078f7c6 | -3.47266 | -54.69624 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cfba870-36ca-34e1-b1b3-b79b5272b6e7 | -9.95463 | -45.32345 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ec5a305-529d-3068-a2be-bbc76dfd9fe5 | -4.56799 | -54.91064 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c44ca385-c2d4-371c-8f1c-97ba278c6e98 | -6.8278 | -59.18161 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a26535d4-4253-3f0b-b174-36d8d5f0417e | -3.76138 | -51.14162 | 2026-09-17 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e119a54-cb7e-3589-88ee-bec55cdef563 | -7.37189 | -44.47977 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 385b6a96-66d2-3d9c-b1c4-edaf1b1564b7 | -6.93938 | -52.59164 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b9c1e8e-0e3f-3029-97f9-a3267c5c5536 | -5.14649 | -55.9397 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0389a8b7-594a-37cf-97e3-bc37a4e8cb80 | -5.79844 | -47.24229 | 2026-09-17 05:16:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5bd87096-7b77-3c01-adab-0b247fc167cc | -10.39607 | -46.63285 | 2026-09-17 05:16:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d933575c-145e-3384-a220-928ec743cfb0 | -6.37335 | -58.28596 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afa6d20e-4289-399e-bd86-5027ab893f8b | -10.39651 | -46.62926 | 2026-09-17 05:16:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4eaeb17d-1ad1-3432-8107-04de9b04df82 | -8.48363 | -57.63767 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 40dbf73f-e483-3175-b922-077cab7c0827 | -4.50814 | -54.9725 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c0f7816e-6615-34d7-9e06-84c2715f27fc | -5.76273 | -45.10129 | 2026-09-17 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 112cd3a6-42ee-32a5-8ba6-37d5449dcefa | -10.11524 | -45.57133 | 2026-09-17 05:16:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55219d5b-d7a7-359a-a058-17251d84f819 | -4.52768 | -55.65993 | 2026-09-17 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78334041-f1b2-3f49-867b-db332ac3701d | -4.57798 | -54.91216 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85d684f9-fc5e-33f0-8e7f-3df3b5764cd7 | -6.79862 | -59.17681 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36f38249-8732-31c8-8eb2-227b68d74fb4 | -3.02149 | -51.34091 | 2026-09-17 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37e2c3b1-c25f-36d1-b1f6-21985088302f | -9.55915 | -46.59207 | 2026-09-17 05:16:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2db0eac7-8274-3b87-9990-7f0fce64766c | -5.97669 | -55.3567 | 2026-09-17 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd3145b7-7f1c-301b-8b76-04c53712b842 | -8.55877 | -44.55502 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 195e5c41-3b68-39c3-8456-4b64faec1d5c | -5.83582 | -52.09442 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6d511c9f-64f1-3e76-8dae-265b9876fce3 | -9.57282 | -46.57506 | 2026-09-17 05:16:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f71ff48d-511a-3656-91dc-fed331d0dc09 | -9.03943 | -47.76284 | 2026-09-17 05:16:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ad63580-89d4-3907-987a-d8ff67ef21de | -7.99981 | -61.37612 | 2026-09-17 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6893d64-b59b-3e0c-abf6-6024a3151c31 | -3.54823 | -48.17869 | 2026-09-17 05:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37664e2b-f1b5-3e02-9b58-d0ab3c2367c6 | -8.47534 | -46.88778 | 2026-09-17 05:16:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a050e0b-58d8-382c-91e9-7923df15f48d | -7.85994 | -54.70047 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 795676b0-db98-344f-9a58-11cbca3fbba8 | -8.49597 | -57.64717 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e50b81b4-9ce5-33b9-8cb8-a2288729ab6f | -2.91144 | -54.1805 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 996d92c0-8b76-3e73-ae3a-2b5391fc0334 | -9.61557 | -45.35037 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9e897c8-7924-3cb9-9b4e-b1d5ff36c742 | -1.81456 | -54.93089 | 2026-09-17 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9a65f21-d2d3-3262-b306-ed3ab41ec387 | -4.45463 | -55.43925 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29befe2f-afaa-3e30-90f3-446268252057 | -5.6755 | -51.9353 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3457d2ff-9f3a-3d8e-9893-2f190b0a6786 | -4.49258 | -55.4948 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac564b16-1ec3-371e-af9b-2906ff39f994 | -8.22513 | -55.46694 | 2026-09-17 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b91ef98-fe36-3d2c-afad-9a53575419e9 | -5.82202 | -52.11018 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 585fb05b-7e3d-3fb6-85f3-fa2095338575 | -5.14926 | -55.9437 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a094b64b-e165-3b26-a214-0181556f75a4 | -7.27351 | -44.20885 | 2026-09-17 05:16:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13d34478-98e5-3c42-84f0-ecdd02cdd335 | -6.66722 | -50.90525 | 2026-09-17 05:16:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8a80783-d5a5-36e0-8c4f-3c1098c6ad50 | -2.87828 | -51.87844 | 2026-09-17 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63744062-a823-30da-8a0d-5fba91e2020b | -5.86051 | -52.05748 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fb6414c-a3ee-31ac-8241-3d7aa6c163ae | -4.50869 | -54.96904 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 856777d4-962e-3b3c-874c-eb7cfac89d1e | -6.82051 | -59.18037 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9b19b7b-bf25-32ae-ac05-298e30c93e6d | -6.08559 | -55.54506 | 2026-09-17 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 504491a2-de54-309d-ba4c-518b5ac7bc1a | -9.11892 | -45.72248 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 96254254-8ad0-3500-88a4-6aa2422e7ed9 | -4.09439 | -53.98693 | 2026-09-17 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3c2b3d74-0e96-3d92-989a-23be6b5c1ecb | -8.57786 | -44.57844 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| af5ee468-189f-3a7d-80c0-044b5574ac6b | -7.58647 | -46.33757 | 2026-09-17 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df6603ec-317a-37b1-9571-4ce611ca97e0 | -7.09294 | -41.83741 | 2026-09-17 05:16:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c758700d-de0d-3f00-9732-4f59d204d8ec | -8.49098 | -57.63515 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f00f5cb1-37fe-3e74-a938-261eb647c411 | -6.10395 | -57.63794 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdacf050-f1cc-3903-93c7-c6e5a1fe4a0c | -6.70042 | -44.14388 | 2026-09-17 05:16:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15d28c17-6663-308b-9427-84348f69c384 | -6.4411 | -60.00766 | 2026-09-17 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b9b72b9-5749-3cb9-90e1-0c03cdcc7345 | -4.57465 | -54.91166 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a52cae6-3a41-38e5-aae8-6577746bbc1c | -4.56117 | -42.94519 | 2026-09-17 05:16:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d96a61b7-b45c-30b4-b073-0b919f1ca6d3 | -6.36281 | -58.28423 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 507b1c37-53f4-3b97-ab8e-738bbea32ab3 | -8.48861 | -57.64971 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README65.md)
