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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a55d59b1-3569-3e78-b2d5-13337fa9b9bb | -12.84905 | -50.66875 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0b27131-ca1f-312b-90a6-1301f21d450d | -13.0421 | -43.22208 | 2025-10-14 04:06:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0fff097b-ee28-3bb8-a675-869e61d26b0f | -11.66674 | -41.44533 | 2025-10-14 04:06:00 | NPP-375D | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 475bbc1a-1307-358f-82d1-c384c0a35c0d | -9.49042 | -43.06495 | 2025-10-14 04:06:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 34a7edcd-e805-37be-adba-ab21980ff9c1 | -11.51762 | -43.51588 | 2025-10-14 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09d711df-530b-3fa4-ac82-6cb28da27142 | -12.02258 | -47.80123 | 2025-10-14 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2ea2d2f6-0232-38e0-8566-98f3648aeabe | -12.8352 | -50.65559 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 102d4c24-725c-326c-91ae-bdacd0e41357 | -13.53505 | -43.01072 | 2025-10-14 04:06:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 82595722-68da-309f-8c10-c6de79afd502 | -10.80839 | -43.95334 | 2025-10-14 04:06:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b1108c3-4993-36eb-9eb7-541221981fe6 | -12.83324 | -50.66552 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4fc07565-f864-3143-bbf5-58a2740384bf | -10.81486 | -43.95873 | 2025-10-14 04:06:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d9684e7-e67f-383a-8a2b-9bb11bbd21ab | -12.81545 | -50.64468 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1261814a-7f22-3f6b-b0d0-7cfad20d3c27 | -12.85818 | -50.65001 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 70a01383-7627-3acf-bf6b-db8de1ade025 | -11.54807 | -43.14963 | 2025-10-14 04:06:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d15fd22a-32ad-3281-9421-2f0886773c7e | -12.81554 | -50.65099 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7fb5ec88-662b-3adf-a7d2-3145e87ef652 | -10.56762 | -44.52166 | 2025-10-14 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cabec1e-168f-337f-9de2-c931117b2e5d | -13.15092 | -42.55278 | 2025-10-14 04:06:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0018c5e0-b2ab-3b24-8b99-963ef538b520 | -12.82597 | -50.64684 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a42be7fb-1112-394b-af47-1151eb9458fe | -14.48208 | -41.45671 | 2025-10-14 04:06:00 | NPP-375D | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6eeafa03-4ac9-3326-a68f-3e6afd6fd4f9 | -12.84831 | -50.64455 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 07c7aa1b-8b5e-3f89-b35d-0868c5adb454 | -13.53904 | -43.00761 | 2025-10-14 04:06:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 1846fc2b-690e-3bcd-ad95-c82b7660d80d | -12.81875 | -50.65566 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cdb1e0ba-9d02-3cdd-a03c-3bc2ec3e28df | -15.03165 | -42.26176 | 2025-10-14 04:06:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3eef4803-d7de-3ad9-b68f-2ca5bd84fc5a | -12.8574 | -43.81742 | 2025-10-14 04:06:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa7985f4-b7e6-3b3f-83b9-0ef9ef3e6b54 | -11.51413 | -43.51529 | 2025-10-14 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 70ec8183-de1b-3ce4-b1b4-8f9f37a68ef4 | -10.73391 | -42.72257 | 2025-10-14 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 524664e0-25b8-3e16-906b-cf201e965a02 | -15.81983 | -41.89609 | 2025-10-14 04:06:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b3e59c1-9edf-3e8c-ae39-753c4bb22076 | -11.55151 | -43.15022 | 2025-10-14 04:06:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6532c3fa-eb71-31e0-b0b2-314a385c2490 | -12.83189 | -50.64462 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1d8f6843-c071-3b0f-8c5e-d1c59912619e | -11.52227 | -49.93616 | 2025-10-14 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fa5594c-5e79-397b-9931-204c4c8c395d | -12.82418 | -50.66314 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3190c55b-f3e4-304f-8921-8fc150f9d309 | -19.82757 | -42.43785 | 2025-10-14 04:08:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1ce0a09b-66bf-3d41-b790-47a967201de9 | -15.79393 | -43.25909 | 2025-10-14 04:08:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0a121c0-4310-3668-83c3-24fe631c4949 | -15.78356 | -43.28015 | 2025-10-14 04:08:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4f62c10-11b1-3dc5-a9a5-14b27e0d431b | -16.1468 | -43.27846 | 2025-10-14 04:08:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49d064d7-0416-33f5-8592-1035be9459db | -15.78996 | -43.26223 | 2025-10-14 04:08:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc87cdd4-5538-326a-baea-01bdef853c53 | -19.78454 | -42.37429 | 2025-10-14 04:08:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 345672fe-2bff-3582-ad4d-be18eb44b527 | -18.0544 | -39.96053 | 2025-10-14 04:08:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0ec00b90-c6c0-3aa4-a84b-948e35b09662 | -19.84258 | -42.45184 | 2025-10-14 04:08:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1e182f43-6e53-32a3-8bbf-35d84d2e9f0d | -17.28598 | -41.46069 | 2025-10-14 04:08:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5c092176-b249-39b8-b7aa-b5bf78ce8c6e | -16.33308 | -41.68459 | 2025-10-14 04:08:00 | NPP-375D | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e3464a6e-2643-3004-8058-10e40e030659 | -15.7979 | -43.25598 | 2025-10-14 04:08:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0ce154e5-bb21-3f56-8da6-fe86f0a55035 | -19.82921 | -42.44948 | 2025-10-14 04:08:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5efab9f5-16cb-36cd-8a65-cf135f272b80 | -16.2391 | -44.05428 | 2025-10-14 04:08:00 | NPP-375D | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fb1513c5-9bc2-3368-bb64-0106d1f1ad0c | -19.82423 | -42.43724 | 2025-10-14 04:08:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| faa936c9-9a73-38a8-95aa-ee2ce48d1575 | -15.79057 | -43.25853 | 2025-10-14 04:08:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef0ca623-41f9-3fd7-b750-3c34e68fee1c | -16.26109 | -42.26802 | 2025-10-14 04:08:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c360c581-e7af-3808-8f9a-a2b783c118dd | -16.65338 | -42.75974 | 2025-10-14 04:08:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 503e178f-8b0c-37e9-8a35-cf4eb8764aae | -16.35099 | -42.38255 | 2025-10-14 04:08:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6f5d0b8-0dbf-3484-8d67-a453824752c8 | -16.89561 | -41.4549 | 2025-10-14 04:08:00 | NPP-375D | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c5b3630c-8bde-3ea4-b347-bba45f13652f | -19.78789 | -42.37485 | 2025-10-14 04:08:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| e57ae3fb-8344-340f-b0ca-83ced2ed9c21 | -16.26043 | -43.18079 | 2025-10-14 04:08:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 20bb0afe-a029-3e51-a405-9f381b82bd10 | -15.73001 | -43.15834 | 2025-10-14 04:08:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d33895aa-838f-3d95-a1ed-d20ce96c5623 | -16.08137 | -41.44963 | 2025-10-14 04:08:00 | NPP-375D | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bd517353-83a5-3b3f-af23-933a32f4968f | -15.66262 | -43.90405 | 2025-10-14 04:08:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1b41ef0-0eab-324d-9d45-8bddd98be7e6 | -16.92023 | -41.68359 | 2025-10-14 04:08:00 | NPP-375D | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7c10a74f-f8a3-3564-957d-408275d8a41c | -16.23846 | -44.05812 | 2025-10-14 04:08:00 | NPP-375D | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cf0d1278-b4e8-3df0-ad4a-b5301c9ed7cb | -16.65005 | -42.75916 | 2025-10-14 04:08:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ee7ad38-3fee-3f2b-a68c-3f0d16fec4d1 | -15.66344 | -43.90508 | 2025-10-14 04:08:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f8b5a02-090b-380f-96f3-d738cb30c10f | -19.82978 | -42.44579 | 2025-10-14 04:08:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1f4ab962-3843-3925-a214-228e9b536e13 | -16.14621 | -43.28212 | 2025-10-14 04:08:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d525a83-a0e9-3cb1-b6cc-488558e5152b | -16.08081 | -41.45327 | 2025-10-14 04:08:00 | NPP-375D | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| f17302d9-9020-3051-9cc6-a1bf063a91d7 | -19.84591 | -42.45245 | 2025-10-14 04:08:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b65aaf97-b4d1-3111-9d50-4283bf8ea5ac | -16.24188 | -44.05872 | 2025-10-14 04:08:00 | NPP-375D | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2d444437-a46e-3642-be20-9acf6dfc5371 | -16.24251 | -44.05489 | 2025-10-14 04:08:00 | NPP-375D | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3b51b673-acbc-3551-963f-780a65e056a3 | -16.52325 | -43.90117 | 2025-10-14 04:08:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e78870da-8708-3f26-847c-40be35588391 | -16.19694 | -43.6747 | 2025-10-14 04:08:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20dae7a4-7688-35da-88b1-3db0cdc77c95 | -16.89897 | -41.45542 | 2025-10-14 04:08:00 | NPP-375D | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 54834b73-5d19-3acd-a735-fa5d224a88fa | -7.9253 | -44.1169 | 2025-10-14 04:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 8e22bc2f-553c-3068-81f6-b6f1b44b750b | -7.9442 | -44.115 | 2025-10-14 04:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 137.7 |
| bedf08f2-ea33-3aaf-b06a-e9e05e7e6190 | -7.9439 | -44.1381 | 2025-10-14 04:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 8d7ade4e-d97c-3e26-9acb-d638bbe814e2 | -7.3942 | -39.7845 | 2025-10-14 04:10:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 37.6 |
| 47458de5-1936-337d-8ed8-a2f4ac9b906b | -4.6696 | -43.1326 | 2025-10-14 04:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| d7a5d6eb-418a-3bcb-9f34-bcd53d546e2b | -4.6509 | -43.1337 | 2025-10-14 04:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 899b51fb-60b3-3be9-94cd-3b7e0ee659c6 | -28.67505 | -49.40284 | 2025-10-14 04:10:00 | NPP-375D | CRICIÚMA | SANTA CATARINA | Brasil | 4204608 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| af540c94-869a-324d-992a-e781dcde9265 | -27.07197 | -48.97327 | 2025-10-14 04:10:00 | NPP-375D | GUABIRUBA | SANTA CATARINA | Brasil | 4206306 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 707aa4a0-279a-3109-9fbd-661beff073e9 | -25.85494 | -50.40332 | 2025-10-14 04:10:00 | NPP-375D | SÃO MATEUS DO SUL | PARANÁ | Brasil | 4125605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 3d08fd51-c550-3520-b808-c3fe8f59e0ca | -27.44294 | -48.45205 | 2025-10-14 04:10:00 | NPP-375D | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| da4e6b25-d025-3379-b8da-2cd362aad861 | -25.40601 | -49.53545 | 2025-10-14 04:10:00 | NPP-375D | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3952daa2-f092-338d-873d-9c561d20a946 | -25.40713 | -49.53337 | 2025-10-14 04:10:00 | NPP-375D | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 26418b92-d67a-37e0-91bb-a47a1284eb4f | -23.4847 | -45.87576 | 2025-10-14 04:10:00 | NPP-375D | SANTA BRANCA | SÃO PAULO | Brasil | 3546009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4d644cd6-95dd-340e-926e-2a417703daf2 | -27.08127 | -49.02644 | 2025-10-14 04:10:00 | NPP-375D | GUABIRUBA | SANTA CATARINA | Brasil | 4206306 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3180b8c5-1a77-319d-a5db-a6a999a24c45 | -7.9631 | -44.113 | 2025-10-14 04:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 458ab03f-f22e-379b-8275-46b9e294a5db | -7.9253 | -44.1169 | 2025-10-14 04:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 94.0 |
| b628a0ec-b72f-33b0-96dd-cb74c43eaef0 | -4.6696 | -43.1326 | 2025-10-14 04:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 0621a486-c381-37a3-ad21-1ea6965f4b43 | -7.9439 | -44.1381 | 2025-10-14 04:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 080261c4-f864-31cf-bdd4-6363580f33c6 | -4.6509 | -43.1337 | 2025-10-14 04:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| b94a6f03-ac7f-31de-8d08-47dcb391c3f4 | -4.8408 | -42.77 | 2025-10-14 04:20:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 0a4d803c-3f09-33dd-a5b1-118fd143060d | -7.9442 | -44.115 | 2025-10-14 04:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 139.8 |
| d91163aa-487a-33d6-8587-cd93ea25f270 | 1.05497 | -51.2382 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efc82366-a6fd-39d2-81bc-9d2f2feab9bc | 1.46886 | -50.87266 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3596730d-cca6-3976-a21f-de1a0f848c91 | 1.11017 | -50.9897 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 09aeea3b-d2d7-3b34-af43-6551ed932352 | 1.13701 | -50.73124 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65448bf5-70b4-35f2-bbc3-1d984b1474e7 | 1.10568 | -50.99041 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c611c080-85e4-388d-b133-be8933d3d401 | 1.12252 | -50.95126 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6d2fd4c1-b72d-3bec-9bbc-89a7efd96ef3 | 1.13078 | -50.94546 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7dc14355-6050-3902-9a95-920f8273f9ab | 1.46307 | -50.88117 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51dc5066-65d6-302e-8af7-3287fef19c81 | 1.45295 | -50.84631 | 2025-10-14 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59978ba7-d094-3982-a4ae-f81b37c03bd6 | 1.82224 | -56.02074 | 2025-10-14 04:21:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60ead5bf-efa5-3ddb-a473-fcdea7b79f71 | 1.82144 | -56.0156 | 2025-10-14 04:21:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README23.md)
