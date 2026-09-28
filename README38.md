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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfbf1ac9-d6c4-3c3d-bc40-f22da250f834 | -7.50142 | -55.01835 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4fd6633-bb00-3b66-b263-1c2167d4e17a | -6.67787 | -45.62525 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 93e31065-8c78-344d-9a5c-90aa562053d2 | -8.36588 | -44.16455 | 2026-09-28 04:34:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5b6673d-9482-31fd-aab3-ffa583aa880f | -10.13973 | -43.89864 | 2026-09-28 04:34:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c3bacaf-3608-3032-ba51-990de64f2eec | -11.6966 | -50.59753 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d3f99ee9-7771-354d-bfac-9a84424473ca | -7.27729 | -55.57808 | 2026-09-28 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c8881f2-e487-3bb9-a525-054633a0633d | -11.36243 | -47.43564 | 2026-09-28 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1d54d78-d0f9-3fdf-9ec1-f8004ae831f7 | -6.65466 | -55.11409 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3212b20a-6cd8-3f64-8f7f-3776ba4fd9db | -8.24847 | -45.40185 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21039a42-5648-39fb-8b90-47df51f6bad1 | -10.11323 | -50.19754 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 262c28fa-aea8-3a20-906f-439979d9e6a1 | -10.21668 | -50.00118 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e2ef89a-c3ad-3d5b-b563-09c1ac97f88f | -12.6057 | -51.96124 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c991400-1ce3-3b67-a02f-8c2ebb6cbc87 | -11.42905 | -47.41522 | 2026-09-28 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 77e8a095-d657-326a-87c7-fd0494c68c24 | -11.20798 | -44.78677 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 231e6961-f8e4-3755-bba4-644ba227b18f | -10.82522 | -57.19843 | 2026-09-28 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c549fb27-3c89-34ea-a8ed-60b8b3b39858 | -11.45264 | -44.93732 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f7a2cb9d-46c5-3262-8f92-331d56d24386 | -8.24011 | -45.40893 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7716e38d-abc4-3736-b215-a9aef98d61b3 | -6.3813 | -44.84335 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed3cfd65-d183-3eac-a7e4-f62a69ad6e85 | -6.0821 | -57.80421 | 2026-09-28 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0144e089-2075-3d7e-99fb-3fdf9ae74a38 | -11.59996 | -44.13104 | 2026-09-28 04:34:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ebec47e7-3d4e-3dde-bf80-e32ce4731af4 | -10.82045 | -61.42145 | 2026-09-28 04:34:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6dc98240-41b7-37cd-8557-68dbda2d24f4 | -12.71306 | -47.30938 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99fb0d2b-3812-3554-9884-705e09033881 | -11.4533 | -44.93254 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f588cd60-e2fd-34ff-b79c-806ce5aa446b | -10.93607 | -50.67052 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5b57341b-f9df-3340-817d-e115eb711221 | -12.59809 | -51.96399 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66a0647b-bc5a-3df6-a64e-50e58699d4cf | -9.02246 | -49.65462 | 2026-09-28 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 750a8574-555d-32db-8c2a-b6b367adffde | -10.37714 | -44.97218 | 2026-09-28 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93ad485a-a318-346c-84ee-2535c34f7216 | -6.71511 | -45.59115 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2b002ea4-87f2-3770-a1c0-f0a24dd5fdf8 | -11.70554 | -44.52703 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9376e3ff-d892-3716-8630-e3f0ee725d69 | -5.30038 | -49.97049 | 2026-09-28 04:34:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| deead3da-b446-3828-85ea-e107cc1cc28d | -7.38207 | -42.10702 | 2026-09-28 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 54126091-a993-31b2-9512-17b4d73323f4 | -10.94791 | -43.88923 | 2026-09-28 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de0e31cc-ad48-3583-bd9f-7cb14ff14429 | -6.35559 | -45.79052 | 2026-09-28 04:34:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad23630b-9a39-31a7-9f9c-ad8eb45822e7 | -12.74349 | -47.78465 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 880f1efa-68f1-3bdf-9e2c-4881bed0b5ec | -6.084 | -57.79369 | 2026-09-28 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| fccc1ef5-d2ad-3a19-a53c-f6fecf1c8151 | -9.62191 | -55.11183 | 2026-09-28 04:34:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e2a9d50-c3f1-3273-9a53-31daf25c35c6 | -9.20088 | -45.76453 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df19e3c8-edf8-3acf-b1aa-a559fdff694a | -11.84273 | -50.49517 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6e9e67e0-0028-3506-b705-f19bbe4fcf75 | -9.74831 | -48.95673 | 2026-09-28 04:34:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f00743f-1de1-3be3-87a6-375b6dcc3d3d | -9.74501 | -48.95621 | 2026-09-28 04:34:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95742c91-f0c0-3d8b-8495-fc430bb292fe | -10.22341 | -49.98034 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33557b82-64f5-3523-9e3f-f61651fd3f2e | -11.40253 | -45.37836 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6326b435-dd8b-3b53-ba78-a93df5ec6759 | -11.4453 | -44.91473 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb811008-e882-3898-8cf2-adaa9196dfaa | -11.10627 | -51.33286 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d2aee381-c051-3170-a63b-739cfc92efd2 | -9.77686 | -44.84078 | 2026-09-28 04:34:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f83190f-4135-3acf-a196-ab7c72eb147a | -7.49841 | -44.57021 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37a2ae5a-2827-3284-944a-67a279879e95 | -13.15135 | -48.5439 | 2026-09-28 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa87d011-3edf-3553-9ebf-2eae84641dfc | -11.83306 | -44.98577 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9ceb76d-8e46-3365-b929-1ac52e689da2 | -6.6872 | -45.65834 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eee72730-7423-3afe-aefd-1e0e6b526e5e | -10.41998 | -53.82926 | 2026-09-28 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 29fb5965-7876-33da-b5a3-6490d9d0ba52 | -10.1189 | -50.18369 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6bec93e1-05c4-3fe1-b793-95b0b38b9e22 | -9.31648 | -45.38175 | 2026-09-28 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5306175c-ca8c-32b6-92b5-c2600e4b095a | -9.62672 | -43.9599 | 2026-09-28 04:34:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 71ebb804-5ecf-3ff4-bbff-801e0df59eac | -12.31357 | -46.41057 | 2026-09-28 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5b656921-ae81-34e3-b671-c50515889177 | -11.20114 | -47.71569 | 2026-09-28 04:34:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 904dd115-8e19-3145-852c-25babc96891d | -9.9809 | -50.15738 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 909ade0f-58c4-3436-9e19-76001577c5d3 | -8.1421 | -44.45453 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1541fe25-37d5-333c-a509-1c00e0d83c31 | -13.10259 | -47.39793 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae17296b-b183-37db-b2ef-53fc5c7178e8 | -11.13399 | -50.05246 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80d5b08a-d41b-3078-944e-6e780dd9aa18 | -7.8883 | -45.44459 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e538f4c5-b226-3715-aaaf-d4f26befa37a | -7.30751 | -44.60002 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 285b5e5b-277a-3921-bec8-361663e8ce22 | -11.63605 | -43.48891 | 2026-09-28 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c80fdbb-63fa-37ed-8aaf-b385ccd39229 | -7.86779 | -61.18317 | 2026-09-28 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3ab8746a-dc9f-3918-8552-3d7f57c45c64 | -11.38505 | -43.42842 | 2026-09-28 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f703655b-f65a-3a4b-b256-21bc24b532a5 | -7.71077 | -39.35003 | 2026-09-28 04:34:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 359d953e-ab69-33ff-a9c1-1f9b843aad0e | -6.92726 | -42.86204 | 2026-09-28 04:34:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2e9e9088-d4f2-3f09-b3f4-bba320d23668 | -6.9453 | -41.60317 | 2026-09-28 04:34:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1455a944-a4a3-3492-80df-025f14b1e558 | -7.67926 | -44.79184 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7e3c272-2491-32ba-82e8-2855a0a9d52b | -7.38621 | -47.01593 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55de46e5-9b34-304f-ba09-4dfc0becc15d | -12.69241 | -47.32971 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d0e6c54a-30af-3157-828a-5dbfcb4b290d | -9.15497 | -45.63796 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e066f15f-7b1d-33a7-89e0-28c41f14b3a8 | -11.34236 | -47.33745 | 2026-09-28 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0ee65dea-6ecb-37f9-919d-9cfe27f302a5 | -6.66432 | -55.11317 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76cf2a96-a9fd-3472-a321-b1bfc231c149 | -12.62758 | -47.3157 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2311bb1a-e83a-3d39-842b-8bc86638f134 | -8.14276 | -44.44987 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a3a534e1-26bc-3ac1-97b1-aae91c27a1ae | -10.81669 | -60.74947 | 2026-09-28 04:34:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 68b1c72b-b199-30e0-80f0-da144c874925 | -10.4169 | -53.82347 | 2026-09-28 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7b397a0c-9bfa-367f-9a29-f19890414593 | -5.64088 | -50.03889 | 2026-09-28 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45a22fdf-0b19-3025-bec1-aaccef563061 | -5.41918 | -49.17833 | 2026-09-28 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3979f8ad-39e3-3649-aa4a-7c4fa4def83f | -11.10503 | -51.34054 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d66429e4-8e45-3c4d-8fd8-e56a07baf6cd | -8.96418 | -44.16468 | 2026-09-28 04:34:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3feff683-bd59-34f8-aba6-d71fce5da259 | -10.81317 | -60.73932 | 2026-09-28 04:34:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 00ccaac2-58eb-33c8-873b-c3d3dfc05c03 | -11.35389 | -47.4231 | 2026-09-28 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6c17509d-3c5b-3004-8234-926a7aa3e8b2 | -10.81247 | -60.73869 | 2026-09-28 04:34:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 75a3faec-e82f-3cd0-a0d6-b5806d008c30 | -12.85006 | -51.0049 | 2026-09-28 04:34:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f00f110d-909e-3d54-806a-39c0130530ed | -12.63102 | -47.31624 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7d5c259a-6583-3496-b8ff-b77c8a649ab8 | -12.7076 | -46.98652 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 891e9a3e-7074-3478-bf9e-5ffa5fa0d0c9 | -12.63447 | -47.31678 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9180ca81-74e4-3307-b646-1ae72d4ecf7f | -6.4194 | -45.85856 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3bee032-9576-302f-9a6b-93971b6d5134 | -7.40558 | -46.61682 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d759917-6b75-347f-94ba-8d23fef6271a | -10.11381 | -50.19393 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6db1990-aa1d-3ac6-b9a0-79bbd9f4f529 | -8.23112 | -45.44544 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e0852d3-6302-392f-b7ad-2b42e1343154 | -10.92594 | -50.66886 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f75b13cc-6e32-33ef-bed2-a228c2ce0da7 | -7.36992 | -44.7593 | 2026-09-28 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b99e2cf5-f3da-3518-91b7-eaadf00f39cc | -12.31714 | -46.41111 | 2026-09-28 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 53889a3c-dd15-34b8-812f-f4ad3cc18d9e | -12.09894 | -50.29848 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 48131d28-6827-3b0c-9e92-7f8e19c2eb65 | -10.22064 | -49.97624 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6c72e00-fe47-31b4-9c61-a280792d0676 | -13.10667 | -47.41796 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| fa1f5b85-493d-34ab-a767-ece60aec9914 | -8.36959 | -45.46502 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 62f58470-eca8-31ab-8ddc-7ee4d6ed1028 | -10.22398 | -49.97678 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README39.md)
