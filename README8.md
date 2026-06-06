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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 319ee932-781c-3abe-880c-2f1f3b077554 | -11.55336 | -52.80091 | 2026-06-06 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e2991596-d4e7-3d60-bb02-82f378ab30e9 | -14.46065 | -54.8862 | 2026-06-06 04:25:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2cf26ef2-b02e-36e7-8c03-299f53af1735 | -12.49944 | -54.7347 | 2026-06-06 04:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9351901-0589-3a85-814e-b5699ee2293f | -13.95207 | -53.84491 | 2026-06-06 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e415cda8-c51d-32b4-a6f9-1429a03fc99d | -14.23256 | -45.80919 | 2026-06-06 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49522052-6a51-302e-b9fb-ad11dfe3f39e | -12.50616 | -46.27237 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 117b242a-2d71-319a-8e85-54cd48dd2f6b | -11.90444 | -57.0386 | 2026-06-06 04:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0fae33b9-0c0f-3f31-8a52-fb531559304c | -11.54969 | -52.7954 | 2026-06-06 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 14f9a918-54e5-30d1-880e-1078b90a27af | -13.30586 | -43.77325 | 2026-06-06 04:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 638a0501-ebed-384c-85ef-d1d9bce9cad2 | -12.50851 | -46.30132 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 17ab8aa9-8a69-3cfd-91c6-3da718cd9810 | -14.24624 | -47.9775 | 2026-06-06 04:25:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c28f00ac-35a7-39e8-8ec4-faba86121bcf | -11.54516 | -52.79457 | 2026-06-06 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c6abc7bc-f345-3086-b868-6fb89ed2c34d | -13.39903 | -46.59713 | 2026-06-06 04:25:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ec4c136-61ef-31db-ab36-e312d01e6af1 | -12.50337 | -46.29002 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5b6da369-f436-3f5a-b696-fbaaed2af1ad | -14.45949 | -54.89201 | 2026-06-06 04:25:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cdc9790-99d5-3769-a1f8-bd3c8458983f | -16.04736 | -48.00026 | 2026-06-06 04:25:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 29ed6a6d-95aa-3250-81bc-3c569d8a4368 | -19.43704 | -42.56777 | 2026-06-06 04:25:00 | NOAA-20 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8023a01d-745d-39a7-9997-4a7683ea6c4f | -12.73399 | -54.20483 | 2026-06-06 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 260887e8-170e-380d-98d5-aa84ebcda2a8 | -13.40178 | -46.60122 | 2026-06-06 04:25:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 75733963-16e4-3e7c-afa8-e789ef970bee | -14.24289 | -47.97682 | 2026-06-06 04:25:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78313ad2-4ed1-3ed2-9b22-af6851d6beda | -16.59348 | -58.23293 | 2026-06-06 04:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d9573a28-5779-3e88-9c05-6ee4cba2fae0 | -16.59253 | -58.23741 | 2026-06-06 04:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 721047b3-2fdb-3996-97cb-9e0b5400e81e | -16.13695 | -58.49763 | 2026-06-06 04:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0a958110-cc8d-3cfb-a299-2436190294c3 | -12.50449 | -46.28297 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d17e3f5c-ab31-3b3d-a2e8-68f485b01b56 | -14.77202 | -52.68295 | 2026-06-06 04:25:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b039f81b-506a-3a46-bd26-a3a1fd6f428a | -13.88718 | -46.94376 | 2026-06-06 04:25:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6f695067-34e7-312f-ae4b-731c4f8414ae | -17.99815 | -51.14554 | 2026-06-06 04:25:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 586c6b52-a2dd-3486-8e34-32f21aaa4745 | -14.20922 | -57.43138 | 2026-06-06 04:25:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6328e071-7b9f-3ef5-930d-868bef2219fd | -13.95675 | -53.8457 | 2026-06-06 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f0fd391b-7bbd-33ee-be21-c0b2a024fb1b | -12.5135 | -46.29129 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b531f61-1acf-30f8-9462-26df72adfb26 | -13.36195 | -43.19806 | 2026-06-06 04:25:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 336fe2b0-87de-3b81-8453-bc15af53ff20 | -12.51737 | -46.28832 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c0802bc-43bd-36b0-9fd6-c5ab5bbff349 | -17.99599 | -54.2812 | 2026-06-06 04:25:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e3f0d9aa-012f-3e69-bf9f-3d19cd2cc3d3 | -13.49858 | -56.57034 | 2026-06-06 04:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ee5e192-4169-3776-916a-eb0ec6d2a080 | -12.77039 | -59.00623 | 2026-06-06 04:25:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b287c87d-8a45-398c-8f6b-80d60e6f590f | -14.24013 | -47.97253 | 2026-06-06 04:25:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11d57e6d-b9b7-3eef-940c-e4d53e997a3c | -14.22924 | -45.80865 | 2026-06-06 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 99e373b2-b77c-3eb1-ba10-4165aaaab152 | -12.50795 | -46.30484 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3d8144a5-3f14-3b61-848e-729936e30714 | -14.24349 | -47.97318 | 2026-06-06 04:25:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a111be4c-3ed7-31c6-9ea1-5d1bdc02af49 | -16.13794 | -58.49309 | 2026-06-06 04:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f5b1f8d2-7898-3b12-87b4-69f055c93535 | -14.24433 | -58.44583 | 2026-06-06 04:25:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 53917bfa-fbcb-3157-999b-d889f578b2c6 | -16.13599 | -58.49406 | 2026-06-06 04:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 639308a1-18e7-3b15-9f46-707e0310cfae | -13.49299 | -56.56916 | 2026-06-06 04:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f9520741-8dce-3cfb-b488-d7f0eab6912f | -17.30172 | -42.64696 | 2026-06-06 04:25:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9ba9d093-c35e-3e94-91c8-9bfbaf3db8d8 | -11.78891 | -56.99886 | 2026-06-06 04:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd3f5956-ca9d-3acb-b2ba-fec39768bd6b | -19.43528 | -42.5721 | 2026-06-06 04:25:00 | NOAA-20 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5e6f7ac7-03d6-36c7-a9a6-e283838c1e4f | -16.60578 | -47.61993 | 2026-06-06 04:25:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f4330b8f-38d5-3b2c-8ef3-ef72ca8b53c6 | -12.49619 | -46.29245 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e872fe5-cb80-3f31-aa94-c78b5da09e98 | -12.51238 | -46.29834 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33058832-7823-3cc3-a845-47349b214c02 | -12.50006 | -46.28947 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 06fe105b-dbdd-3e3b-9bbf-8e6728d7fd6a | -11.5443 | -52.79929 | 2026-06-06 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 798b843f-8953-399e-bc8f-bb57d5d46141 | -11.63464 | -55.17659 | 2026-06-06 04:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e497439-ce53-37f8-81b3-8d4d61f4fdd0 | -13.49077 | -56.56879 | 2026-06-06 04:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff946c97-4ad6-3665-91fd-992732a7e797 | -12.5052 | -46.30077 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| aef74423-dd76-35bb-9ac6-67b27b10d6f2 | -12.51681 | -46.29184 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 237f7a67-bfe4-34c4-ae03-d45b09dcd5ad | -12.50062 | -46.28595 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0b83cf63-a94f-3297-8c7e-fb8c4b37db2d | -11.56325 | -52.79805 | 2026-06-06 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| df16dc2d-4856-3c4b-b410-6d54ac097127 | -12.50727 | -46.26531 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37e4b2fa-5ec3-38b4-be3d-bfbcb7f8f44d | -16.5969 | -58.23759 | 2026-06-06 04:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 2fe9dde2-3d90-3dd0-b999-afc49b6081ad | -16.13196 | -58.4917 | 2026-06-06 04:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9b3839eb-ff2c-37e3-a981-710211006e65 | -14.76779 | -52.68203 | 2026-06-06 04:25:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89abfc19-b3fe-34a7-832f-84b16a1222ed | -18.00485 | -54.28319 | 2026-06-06 04:25:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 22d8584d-d182-3df8-9563-ba393c9c8173 | -12.51631 | -46.27367 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c01b5b3-e8ed-3f87-bd1e-8c4b59797df3 | -11.05167 | -56.92243 | 2026-06-06 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2f6c519-19e0-30f9-b891-897e918652f8 | -11.634 | -55.17989 | 2026-06-06 04:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 370a6128-affb-33e6-9487-c6cc7e2d10a5 | -11.78552 | -57.00043 | 2026-06-06 04:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 891f6c8e-cb6e-3216-9f19-d2dfcbe14de7 | -18.51769 | -48.34345 | 2026-06-06 04:25:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b35d373-a6e6-391a-b9ea-12a3a71be0df | -14.23617 | -47.97551 | 2026-06-06 04:25:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a301f89c-657d-3b18-b427-be143377bd98 | -11.72379 | -56.84154 | 2026-06-06 04:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d74eecb3-396c-36d0-9084-b5ecbdd40e18 | -12.92838 | -43.62016 | 2026-06-06 04:25:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3294b7ec-9110-3e63-b92a-c515c7839af3 | -16.59837 | -58.23876 | 2026-06-06 04:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 528ec8b6-b99b-3a28-989f-39178528cb15 | -14.22426 | -45.79682 | 2026-06-06 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| acc2b479-8beb-3dca-8581-5a46bafa0bc5 | -11.05079 | -56.92681 | 2026-06-06 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b23ac44-cff6-30ff-baf5-ddaaa5d6feb0 | -11.55507 | -52.79158 | 2026-06-06 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| edeca5aa-27d3-3a94-a768-b2fd6c78c233 | -17.60525 | -46.66703 | 2026-06-06 04:25:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ce77c3f9-d49a-3d02-b9dd-636dde0c1f74 | -14.25155 | -58.4422 | 2026-06-06 04:25:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 15c393f9-dcfa-309e-8ceb-06067bb829c0 | -19.44106 | -42.56825 | 2026-06-06 04:25:00 | NOAA-20 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 18e839f8-1776-3493-bf3f-8ca33275b94b | -18.86688 | -47.65104 | 2026-06-06 04:25:00 | NOAA-20 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca523622-9418-3bf4-a695-fa5865e970db | -12.50281 | -46.29354 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b1d2cf27-3294-3237-ada6-f2d96a0ceae1 | -14.2237 | -45.80041 | 2026-06-06 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ffc53a0e-a575-3ed6-98fb-e4bb1848a56e | -11.05425 | -56.92849 | 2026-06-06 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ee11b37-516a-3305-917b-5d2de96d4539 | -12.52017 | -46.27071 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66319fc9-1900-36cc-9f74-6c317b08476a | -14.2101 | -57.42716 | 2026-06-06 04:25:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa8f85db-3d19-38c8-ae12-9bba6a172344 | -14.23953 | -47.97614 | 2026-06-06 04:25:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ad657f5-366a-3906-b398-3efba29f7612 | -13.30646 | -43.76928 | 2026-06-06 04:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3dcef719-ca69-3e2e-b63f-d7f2cf018e60 | -11.0491 | -56.92307 | 2026-06-06 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9cc8a7c3-3ca1-3737-b712-cf7ad7fd9f67 | -12.09697 | -52.00625 | 2026-06-06 04:25:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e36d019-2ae4-3438-b77d-dab27ec954bb | -14.65908 | -49.1587 | 2026-06-06 04:25:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1b9e3d3-3e3e-3dd4-b0de-048097d4d9cf | -18.86745 | -47.6474 | 2026-06-06 04:25:00 | NOAA-20 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fdf69cf-0614-3bfb-9fbf-b72e7c325bf1 | -15.31392 | -41.89843 | 2026-06-06 04:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 1801b686-8564-3f00-9a77-a9d059fa909e | -11.55958 | -52.79248 | 2026-06-06 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a25c1fbb-0462-3fca-b7c8-363dccadbd06 | -12.73504 | -54.19923 | 2026-06-06 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac625f80-6ac2-3e0a-b999-c0d859a51b0b | -13.95444 | -53.95994 | 2026-06-06 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55a75fd3-c5b6-32ee-84d7-843aec9c30c5 | -11.72262 | -56.83821 | 2026-06-06 04:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57974b94-79ef-3a67-9781-4aefe838d50e | -11.79237 | -56.99704 | 2026-06-06 04:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc4ef6e0-ac88-36ad-9da8-ff8ec61b3b93 | -13.39847 | -46.60067 | 2026-06-06 04:25:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aea6798b-6a85-3a7d-b722-e9622dbdf5fc | -17.30628 | -42.64241 | 2026-06-06 04:25:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 19ef6e43-40fb-3d6c-b66a-00840f6b23d5 | -11.26509 | -53.96893 | 2026-06-06 04:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bda4512f-b9af-3e73-9ed6-c5132053c89a | -12.51961 | -46.27423 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd2c4c8e-faa5-3dc7-ba61-cd64d7dcab95 | -12.49675 | -46.28893 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README9.md)
