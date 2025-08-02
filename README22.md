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
| 8f7a8000-7faf-3083-a934-cf995f4a0337 | -15.11053 | -55.21399 | 2025-08-02 05:14:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| dff494cb-dda8-31b2-bc70-50afd851faf8 | -13.99004 | -53.92776 | 2025-08-02 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8854deb3-eba3-3d55-88e1-891b26126ecf | -10.45743 | -46.99156 | 2025-08-02 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6df938a-7ba3-3ddb-b77a-2b8752dc9416 | -10.03027 | -44.71516 | 2025-08-02 05:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c292e30c-01c2-329b-b89e-b6c661c400b2 | -15.75544 | -49.94872 | 2025-08-02 05:14:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8254f123-5556-379d-bba3-1d1aa13ef22b | -15.75503 | -49.95228 | 2025-08-02 05:14:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3fb98784-dfb4-3f35-8e5e-478bebeccfd1 | -13.22346 | -47.24962 | 2025-08-02 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f304c429-200b-3a36-b465-ae5167f11140 | -11.95856 | -46.66614 | 2025-08-02 05:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 897be532-3ceb-37dc-b318-acc01e1b5e27 | -12.26146 | -60.65551 | 2025-08-02 05:14:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6dba55f7-e0f7-3d70-8c43-503a8d5c1497 | -16.70093 | -49.39654 | 2025-08-02 05:14:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 268bd92e-7210-3872-a657-e4c633fe5521 | -11.41319 | -56.86715 | 2025-08-02 05:14:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09a7a017-4cc4-3196-890e-2d669d265770 | -11.95001 | -46.6706 | 2025-08-02 05:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d8325ce-2989-3f02-8b8c-cdfe0d2de42f | -13.23346 | -47.23283 | 2025-08-02 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9182627d-8810-3589-b1d4-3d29efff898d | -13.97998 | -53.94088 | 2025-08-02 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 28645e9e-5ec2-37dc-9ed2-65cece0e845f | -10.04194 | -44.71829 | 2025-08-02 05:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad630f61-aea7-3c0f-b374-903297b71626 | -13.04568 | -46.75426 | 2025-08-02 05:14:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5399b41d-8abf-3195-92cc-c687dce153cd | -12.66788 | -44.4855 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3f4a6177-9af3-339e-852f-6a6107a5866b | -12.66806 | -44.54038 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ec1ead94-cadc-3324-b4d6-bbab9935a155 | -12.66159 | -44.53213 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d489c827-38fb-3858-8693-b63f94b49006 | -12.66695 | -48.09814 | 2025-08-02 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9347a119-946a-3667-a69e-8c33bd5fb11f | -11.19342 | -51.51395 | 2025-08-02 05:14:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3cde04f9-7423-3858-812d-5b061607affa | -12.66639 | -44.50032 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 817a682e-25d1-3d8a-9935-17e493382a18 | -12.66316 | -44.51744 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cc2b4a94-f185-39e9-b4b7-dfb8ebf5f8b7 | -10.64489 | -45.23899 | 2025-08-02 05:14:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 487e8e6c-3f15-349c-8846-107f05d8b2e2 | -11.9452 | -46.67019 | 2025-08-02 05:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fac17940-646b-3834-8575-b08582d41412 | -12.65433 | -44.53123 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f4f12841-fb4c-316e-8aa0-19f1a551e436 | -15.1245 | -55.22512 | 2025-08-02 05:14:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b4bc551-692e-32fe-ac31-4a7eaede8502 | -13.23251 | -47.24104 | 2025-08-02 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96ad698c-a666-3b9e-a7ff-6bb4c3b6bb71 | -13.23153 | -47.23361 | 2025-08-02 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef6a687e-ab7d-3dcf-94b7-9321c11b9dc2 | -10.03726 | -44.71604 | 2025-08-02 05:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 99c218b7-b5eb-3d23-ac7a-267405434679 | -12.66885 | -44.53304 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1425793f-b402-3d16-ac12-96e5cbdfc276 | -14.00004 | -53.94458 | 2025-08-02 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00b1e200-f4fa-3fa0-8f63-d4d1f0037fbf | -10.63875 | -45.23722 | 2025-08-02 05:14:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac227adb-68d5-3cae-8f89-eec2d35815dd | -12.44824 | -47.04583 | 2025-08-02 05:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e96ddee-82f4-3ccb-a9fe-56471f2299cb | -15.11886 | -55.21805 | 2025-08-02 05:14:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2f03cb4-1145-3d2f-a23c-e0e7d08f3ae4 | -12.66395 | -44.51004 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b126a18f-763c-38a7-953d-ce56567e6f48 | -15.11179 | -55.2332 | 2025-08-02 05:14:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 15ddb0da-7cc8-3f4c-8ce1-908a32cfc036 | -15.11433 | -55.21457 | 2025-08-02 05:14:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 691d1bd2-58f9-32b3-a6a0-b454d58d7d93 | -12.66081 | -44.53947 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fea8869b-443b-304a-8417-a456d31d193d | -12.67611 | -44.53392 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 74a8c1dd-dfc9-3de4-947e-52f006b1d332 | -11.35158 | -51.26064 | 2025-08-02 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a8713e2-2e21-3489-828b-3abe54594629 | -12.44087 | -47.05487 | 2025-08-02 05:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6569b94d-7fad-374e-9384-55793ddd68cf | -12.65017 | -44.50108 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 593d3bb3-d2fa-3db3-b82a-338da0c8570c | -15.11751 | -55.21961 | 2025-08-02 05:14:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3eb9541-3419-3c52-913c-cf1c148fc3ed | -15.10811 | -55.21182 | 2025-08-02 05:14:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ce7cf3f4-0b5a-3162-a543-292a520c66f9 | -11.35359 | -51.26466 | 2025-08-02 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11eb9db8-e2d9-30b0-8b91-cf75ac7da19e | -12.67321 | -48.09552 | 2025-08-02 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ea6fdff-24d7-3b63-b367-34e21decc0e7 | -13.06038 | -47.44271 | 2025-08-02 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2298a99-9a8c-3983-ad90-0f89967f6a3b | -11.35625 | -51.26126 | 2025-08-02 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 762387b7-b468-3e71-b5e2-3c44f1c91ee1 | -13.23297 | -47.23708 | 2025-08-02 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a782c7a-ff12-3127-8555-c32f879ebf40 | -13.98302 | -53.94867 | 2025-08-02 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcdffab5-6b72-31b2-bbfd-9a93229031a8 | -12.67141 | -44.5235 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c1677dcf-a0ad-383c-adad-21d9da7e1be6 | -16.71279 | -47.57506 | 2025-08-02 05:14:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2ea23f9-d53f-339a-938d-5b3e095f5e27 | -13.98352 | -53.94507 | 2025-08-02 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa58e632-56f1-3940-b31c-295070ecf73a | -16.70137 | -49.39238 | 2025-08-02 05:14:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a27fc106-8855-3ff8-b590-11388dba1a49 | -13.23065 | -47.24163 | 2025-08-02 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 041f424e-e3e0-3322-8a37-7bc9af34ca38 | -12.66489 | -44.51521 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 708dd5a9-3962-39eb-9588-f2f2999e67c7 | -12.67123 | -44.51084 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fe460426-dbeb-344d-ab98-d3f2bfa6f588 | -10.4626 | -46.94921 | 2025-08-02 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 606e64f1-8471-368f-a0f7-96c83ca12cb5 | -10.46646 | -46.96864 | 2025-08-02 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4bd8a4e6-8dc5-3c4c-8fac-97db5dbeb9e0 | -12.66553 | -44.49522 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3e716470-1ef4-3667-a497-4ab9a0b6fa30 | -12.67793 | -44.53181 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 523d670d-9a91-3864-b746-c875c4e96204 | -15.12202 | -55.22307 | 2025-08-02 05:14:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3bca383-f8b6-351b-ad45-7227cb80c1b5 | -12.65667 | -44.50926 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 70035084-7305-3413-867b-e663a79abeca | -11.90802 | -55.88357 | 2025-08-02 05:14:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a154b5e3-e165-3693-8173-aaf36b536b2d | -12.65825 | -44.49443 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 52d1fd5a-f668-3394-9388-efeb5a4cc4e5 | -18.33561 | -54.28617 | 2025-08-02 05:16:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8808243a-ab58-3c16-9628-1d1b727c76f7 | -20.87681 | -56.37727 | 2025-08-02 05:16:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6379c4de-433e-36c3-aa90-f58ccc363bb6 | -18.33509 | -54.29017 | 2025-08-02 05:16:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a23e4eb6-c52d-3ccb-b52f-caeec518c565 | -23.09237 | -55.19145 | 2025-08-02 05:16:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 14306f96-a25e-3368-896f-df98425b1488 | -20.45429 | -46.4128 | 2025-08-02 05:16:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cb59f086-c50a-32bb-a68f-25330738b2c7 | -21.146 | -48.01532 | 2025-08-02 05:16:00 | NPP-375D | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 09e7a43a-5d5b-3cd1-96d6-b6879e31e3ff | -20.45145 | -46.41901 | 2025-08-02 05:16:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fd4a321a-2383-3f85-b87d-2d0949db7f92 | -20.26806 | -50.54176 | 2025-08-02 05:16:00 | NPP-375D | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 09b66b28-5356-322e-ace8-0e27d43983c3 | -16.99818 | -49.47391 | 2025-08-02 05:16:00 | NPP-375D | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e33b345-0c06-3457-afe1-fe6cd4fcd4fc | -20.26846 | -50.53797 | 2025-08-02 05:16:00 | NPP-375D | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c9c2b5cd-092a-398b-8e5b-f9daff86bcb2 | -22.32102 | -48.71866 | 2025-08-02 05:16:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 14d25ff2-213d-3401-b756-08d8e29074d6 | -18.53024 | -49.49818 | 2025-08-02 05:16:00 | NPP-375D | CACHOEIRA DOURADA | MINAS GERAIS | Brasil | 3109808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| b9d077d7-201c-368c-96ea-2790502cd6ad | -22.32733 | -48.71914 | 2025-08-02 05:16:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7da4b573-808a-3cbd-8ee8-8411481b34e7 | -23.70483 | -51.65173 | 2025-08-02 05:16:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f4d4a1fb-702b-303c-a9c3-7d3d64e4728d | -20.87749 | -56.3723 | 2025-08-02 05:16:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a634271-4ce7-3331-9e5b-f9c454cf1c03 | -22.3246 | -48.71437 | 2025-08-02 05:16:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 388320c4-9fb5-3545-bc8e-5fbc56c13186 | -23.70836 | -51.78366 | 2025-08-02 05:16:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 27ef2fcb-4685-3956-9ee7-cf0732e42a46 | -22.5971 | -54.97379 | 2025-08-02 05:16:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fa996b8a-e5ac-3bdf-836c-7bdd3fdd91b6 | -23.09287 | -55.18721 | 2025-08-02 05:16:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 8989ead7-2228-3b82-a9a3-4bb5b8f21609 | -17.00386 | -49.47449 | 2025-08-02 05:16:00 | NPP-375D | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4144b7c8-df69-3558-b455-cd004a7080f3 | -20.87559 | -56.37471 | 2025-08-02 05:16:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83ff4973-0433-37f7-954f-45e934affe9d | -21.14538 | -48.02061 | 2025-08-02 05:16:00 | NPP-375D | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 73fd2518-37f9-375b-b611-eda452741ecf | -22.66647 | -53.37983 | 2025-08-02 05:16:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8524ad0a-b6ab-346d-a374-8db3a82e55e2 | -21.14556 | -48.0209 | 2025-08-02 05:16:00 | NPP-375D | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d9b33a48-d8fb-32ac-abfb-3ae189799334 | -21.33195 | -55.62856 | 2025-08-02 05:16:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 506c1d13-64a7-3070-b8ac-3139a540cd2b | -23.70801 | -51.78728 | 2025-08-02 05:16:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| db10395c-7952-3ccd-8a6a-18146d288901 | -16.46983 | -54.67937 | 2025-08-02 05:16:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc0e03c5-5e9d-3850-b999-1444be1b2134 | -20.87878 | -56.38022 | 2025-08-02 05:16:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0a2dd1e-8be7-3ff2-9516-af0b76486db1 | -18.33612 | -54.28217 | 2025-08-02 05:16:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 822a56d5-18a7-31f3-b037-e55a60378ef3 | -20.45211 | -46.41034 | 2025-08-02 05:16:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91109c94-9bf8-38ab-b5dd-50047bab0c0c | -23.08863 | -55.18668 | 2025-08-02 05:16:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| aabd3029-8b67-3512-94f6-38b66e322acb | -21.13938 | -48.01436 | 2025-08-02 05:16:00 | NPP-375D | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 787146eb-31c1-3746-a331-3db750a4fec6 | -22.32421 | -48.71944 | 2025-08-02 05:16:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a0df1430-f964-3a61-8344-5cbc5b276c1c | -20.45932 | -46.40899 | 2025-08-02 05:16:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README23.md)
