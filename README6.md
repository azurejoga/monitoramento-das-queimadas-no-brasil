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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19b2aa95-4bf5-366d-977c-6a2809cdb92b | -9.78177 | -48.25526 | 2025-07-05 03:57:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 80c354ff-ccc8-392c-8950-f06cbb0fd121 | -10.56866 | -49.13045 | 2025-07-05 03:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d91d78b6-0e60-3237-8193-fe192de9a9ee | -15.92225 | -43.51477 | 2025-07-05 03:57:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad68028c-4106-3086-90d7-5a51984faadd | -10.36802 | -46.99028 | 2025-07-05 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3305652c-e880-3cd6-a13d-b81b72ecd92d | -14.66616 | -45.37626 | 2025-07-05 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| acf89b9a-2e9e-3c4d-8620-61ff6ef0c808 | -10.36705 | -46.99565 | 2025-07-05 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a902cf2-7cfc-3515-9b34-2136c0c3957e | -10.55693 | -49.13186 | 2025-07-05 03:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 39a4626b-dc75-3132-9a5a-8fbba3628a2f | -7.96373 | -47.23339 | 2025-07-05 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 862a75e1-39cc-3599-b831-38a4656267eb | -10.60571 | -46.42862 | 2025-07-05 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f78e8cf3-a355-33fa-9f5b-b0f27ea05aa2 | -10.65684 | -40.81014 | 2025-07-05 03:57:00 | NPP-375D | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2f5a8b8b-6340-3d1f-b445-da1a094cd513 | -9.58192 | -44.6085 | 2025-07-05 03:57:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2a9cb53d-328d-3548-8960-e18355d2805b | -10.61713 | -46.39088 | 2025-07-05 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17d262e3-ec3e-3475-9ec9-2cddcbafc28c | -15.75483 | -43.37542 | 2025-07-05 03:57:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d8459067-1dc7-3066-b18a-914477e9338e | -11.87457 | -44.8763 | 2025-07-05 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cbd76b2d-5ba6-351f-a5f2-207e69970328 | -7.95918 | -47.22935 | 2025-07-05 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9e75bda-3c3f-3a23-afc3-b78e446e8d03 | -9.84942 | -46.4684 | 2025-07-05 03:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50835f26-63b7-3834-8fc7-814d409fc24f | -11.87094 | -44.84966 | 2025-07-05 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 521a7396-5ab4-327e-935a-e71c0142ec92 | -10.56318 | -49.12917 | 2025-07-05 03:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 24e0da1d-cc6f-35aa-b5b4-b3eae8458e9f | -13.64805 | -46.81099 | 2025-07-05 03:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b11530b7-91d6-3a7e-9499-1ee71f301114 | -10.60913 | -46.42577 | 2025-07-05 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3ce32c99-6e49-30c2-880d-5f4fb08ed52f | -18.339 | -52.04508 | 2025-07-05 04:00:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6926b12-42f9-3697-ab6c-b509560a433c | -19.26234 | -44.42961 | 2025-07-05 04:00:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5458a50a-d50f-34dd-82c4-419ba0df10e8 | -18.85313 | -47.48994 | 2025-07-05 04:00:00 | NPP-375D | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b35875ec-8ec1-3885-92a1-cf964b8bcad8 | -18.03277 | -46.05589 | 2025-07-05 04:00:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e5084fd-442e-3e67-8a93-049403516547 | -19.74981 | -53.9999 | 2025-07-05 04:00:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 811cfac4-69d3-322d-bd15-85cf5c677486 | -20.76199 | -46.76908 | 2025-07-05 04:00:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2de0c3e5-c9c3-3c6b-a2bf-149505f658be | -19.07622 | -43.87482 | 2025-07-05 04:00:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d7a071ad-b686-3b4f-805a-2f15facd2331 | -18.55977 | -46.49786 | 2025-07-05 04:00:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd223b82-cbda-30ff-aa64-e940103c652c | -19.43608 | -44.34096 | 2025-07-05 04:00:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17a49b9b-a747-376b-ba9b-9a950dcd360d | -16.36216 | -46.87826 | 2025-07-05 04:00:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 469ae971-f9f1-3f6c-8b08-3ccd60406578 | -18.8467 | -47.49036 | 2025-07-05 04:00:00 | NPP-375D | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 54b4fa5e-79b7-3309-8294-0c8382273e3c | -20.43719 | -50.72204 | 2025-07-05 04:00:00 | NPP-375D | PALMEIRA D'OESTE | SÃO PAULO | Brasil | 3535200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| af98f045-2b87-35e5-adf8-8ea3e79435ae | -18.45459 | -51.23597 | 2025-07-05 04:00:00 | NPP-375D | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8fbf3036-f258-3617-b9ae-80131ec7b6ec | -16.29773 | -45.1002 | 2025-07-05 04:00:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a93731c3-dae7-357c-8e04-c3c066c49a8a | -19.7522 | -54.00241 | 2025-07-05 04:00:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 256c7db9-7137-384e-a84c-02e4c601cb2a | -18.66332 | -55.74635 | 2025-07-05 04:00:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 14e836eb-40e7-35c2-aa3a-854798c4e0e7 | -19.71696 | -40.35592 | 2025-07-05 04:00:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a7bee80d-8568-3114-a45e-00576a0381a9 | -21.91265 | -42.26124 | 2025-07-05 04:00:00 | NPP-375D | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7afd6b4e-0a13-3f50-9da9-b24d9bacb34d | -21.15355 | -42.97702 | 2025-07-05 04:00:00 | NPP-375D | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 11c5514e-c1c0-3718-ae7e-07792ed491cf | -17.86992 | -45.54592 | 2025-07-05 04:00:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57a7a75c-a574-38a3-9f97-00b98603716b | -18.85093 | -47.49145 | 2025-07-05 04:00:00 | NPP-375D | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d2f6dcb-85ba-3cfe-984c-74fba02cdeaa | -21.471 | -44.48444 | 2025-07-05 04:00:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5a139d3c-f739-33c5-8fe3-306c7a731ae2 | -20.44088 | -50.72977 | 2025-07-05 04:00:00 | NPP-375D | PALMEIRA D'OESTE | SÃO PAULO | Brasil | 3535200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 08ed4c0f-98c6-388a-ba9b-9124a80de64e | -19.53642 | -44.07962 | 2025-07-05 04:00:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 69758721-42b9-34f7-a7cf-e479f091eb49 | -19.74864 | -54.00498 | 2025-07-05 04:00:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b1792620-1fac-3e2a-a714-b3e6b8135137 | -22.12941 | -42.69909 | 2025-07-05 04:00:00 | NPP-375D | SUMIDOURO | RIO DE JANEIRO | Brasil | 3305703 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f5dccbf7-2df3-3e9c-bede-2dd1f1b681d2 | -20.4176 | -43.55504 | 2025-07-05 04:00:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 328fe8df-cab3-3609-affe-377d1bd2f407 | -17.77833 | -42.80815 | 2025-07-05 04:00:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84c08d84-d02d-3f18-b074-74bec2132e1c | -18.03545 | -46.05488 | 2025-07-05 04:00:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92e0ae2d-aae2-3ef8-a953-78be8013148d | -18.8475 | -47.48615 | 2025-07-05 04:00:00 | NPP-375D | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2743e04-d6d5-37a5-9257-50b0a5a9a355 | -18.33328 | -52.04371 | 2025-07-05 04:00:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2972e179-6daf-3868-a67e-f99bc6a67af1 | -20.1745 | -43.71056 | 2025-07-05 04:00:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c494c643-61ea-340e-aa70-1adb849b33a1 | -16.68104 | -43.88475 | 2025-07-05 04:00:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5abea5fe-9ff1-3e9f-9730-750b5c643260 | -21.47158 | -44.48319 | 2025-07-05 04:00:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f29dbcd8-e1f7-343f-a640-5e8b360ace4d | -17.91115 | -45.53856 | 2025-07-05 04:00:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bbc204c0-2c24-3116-83f5-338678339cde | -19.83195 | -42.70392 | 2025-07-05 04:00:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 27e4e45a-a655-3474-926a-c7a3841e15ab | -21.21043 | -48.63479 | 2025-07-05 04:00:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f710be3c-ba1e-349d-9a6e-8dcbb67fc1aa | -15.70033 | -48.30256 | 2025-07-05 04:00:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 920e320c-d10a-3932-988e-3e5f597fba7f | -19.08042 | -43.87132 | 2025-07-05 04:00:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf100ec0-adcd-34d3-8b63-5d9c511d5d7b | -19.71753 | -40.35216 | 2025-07-05 04:00:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2dee4aeb-54b4-3fd8-a372-db7e92f48999 | -18.92357 | -48.34859 | 2025-07-05 04:00:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33db0902-c815-356d-88c8-5aa132d93847 | -19.26159 | -44.43391 | 2025-07-05 04:00:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6f88b8a-8fc5-38e1-8de7-400b853ddbcc | -17.49906 | -44.28117 | 2025-07-05 04:00:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 93c671e1-d6bf-3c71-ae80-4d93b5023fb6 | -19.74602 | -54.0006 | 2025-07-05 04:00:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30910a7b-fd56-32b0-af7c-d6b40562e139 | -18.66735 | -55.74696 | 2025-07-05 04:00:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| aaea82ff-f9cd-3471-80d6-859246698ef8 | -20.42736 | -47.4259 | 2025-07-05 04:00:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35a904b6-b40d-3238-a473-a7c842bd4810 | -19.07692 | -43.87067 | 2025-07-05 04:00:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d84924da-90f7-38de-8986-834019141a9c | -19.07996 | -43.87411 | 2025-07-05 04:00:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e5a4e0d-eda1-3d56-854d-d4a8b6b3e515 | -17.67774 | -43.69843 | 2025-07-05 04:00:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7966a836-94cf-372e-b28b-b8d50021e219 | -17.09571 | -43.80299 | 2025-07-05 04:00:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c52039f-e1ea-3a98-b44b-3b87b20a6803 | -19.07972 | -43.87547 | 2025-07-05 04:00:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23fa8ea5-271d-356c-9b9d-8db30e2f4bbd | -19.43825 | -44.33887 | 2025-07-05 04:00:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b6eab48-e619-323b-ab76-ef2a28ece3a9 | -19.12851 | -52.69187 | 2025-07-05 04:00:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc87ff4a-6e1d-38ab-bc2a-d192346aecfb | -19.98216 | -47.18177 | 2025-07-05 04:00:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d462e62-44cd-3a1c-8335-87bd66443c37 | -20.76595 | -46.76984 | 2025-07-05 04:00:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 37051958-c5ed-3c7d-949c-f9d1e6ac386f | -18.45381 | -51.2396 | 2025-07-05 04:00:00 | NPP-375D | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a7d00bc-1538-3c43-828a-ce183585c8fd | -20.41826 | -43.5511 | 2025-07-05 04:00:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 07ace61b-1302-38a3-b5b4-03c9eacc1fe7 | -21.20938 | -48.66333 | 2025-07-05 04:00:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ec85da2a-923b-3035-b30f-29f855cf37b6 | -18.85173 | -47.48724 | 2025-07-05 04:00:00 | NPP-375D | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 084bc78f-b296-306a-a97c-e2533f00abde | -19.82858 | -42.7033 | 2025-07-05 04:00:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| de6b3db2-9dfa-3081-8a51-c1d99e867d6d | -17.91156 | -45.54023 | 2025-07-05 04:00:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91ed9965-2666-3ba1-9daf-871e3c66eb50 | -18.33238 | -52.0479 | 2025-07-05 04:00:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fac1418d-a478-3e61-8a61-db4430ce9324 | -20.09155 | -44.28297 | 2025-07-05 04:00:00 | NPP-375D | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 976a533c-32a7-3bbf-87db-f173c4428663 | -17.67559 | -43.68976 | 2025-07-05 04:00:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d51705f-3696-36db-bffb-8e2a1a9bb4e4 | -23.594 | -47.43674 | 2025-07-05 04:02:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 469be4e5-6486-3584-b83b-ac65f221c087 | -22.78726 | -43.7576 | 2025-07-05 04:02:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fd6ca34e-bbc6-36fd-9b7c-7086af104117 | -21.89718 | -56.74502 | 2025-07-05 04:02:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd036dbe-cf9a-3d17-b9b4-49fc5e06378c | -21.95186 | -47.37581 | 2025-07-05 04:02:00 | NPP-375D | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 95729cc3-1dfd-3aeb-831a-1385abca013f | -22.85625 | -42.98004 | 2025-07-05 04:02:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ba214be1-7692-3d07-b613-0e55eb69be3a | -20.72949 | -56.65716 | 2025-07-05 04:02:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 793e545d-0ede-33d6-b889-352448a32e84 | -22.53993 | -48.81115 | 2025-07-05 04:02:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9fcaa6d-33a9-388f-9fa2-f21093a89ecd | -20.72217 | -56.65635 | 2025-07-05 04:02:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f28ba352-3a05-358b-9872-115eb6d4ee80 | -22.80537 | -43.12285 | 2025-07-05 04:02:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 55fabb22-4106-3815-be20-397e33338e19 | -21.89206 | -56.73595 | 2025-07-05 04:02:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a969813-d173-3122-815d-7164f9a9cc0b | -21.89605 | -56.74046 | 2025-07-05 04:02:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b7271dc-ca78-33f7-899d-c4a1e0590be4 | -10.6174 | -46.4323 | 2025-07-05 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 1bff2aa2-f62d-34a0-ad2b-f52d2b8c7dc1 | -10.6177 | -46.4098 | 2025-07-05 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 5f8a5d5e-082e-3efb-b11b-15c268a62cac | -5.60406 | -45.18049 | 2025-07-05 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 90b5cf9e-dd92-3bba-acc6-78e510584e15 | -4.39391 | -48.94063 | 2025-07-05 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b6d4a45-1446-3d7a-b88d-a81a1535c7bc | -4.76867 | -45.34816 | 2025-07-05 04:17:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README7.md)
