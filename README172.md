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

## Dados Diários - Página 172

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66e1fc99-5190-300c-9316-dde2725c58bb | -11.76274 | -46.78431 | 2026-10-09 05:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a1faca8-f30f-322f-b692-c71ce74d853c | -13.1617 | -43.27636 | 2026-10-09 05:06:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e075a369-d093-3332-a882-cf4260df4055 | -13.1732 | -54.3123 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a92a7900-3e6d-331c-a6ce-ae707d52ab78 | -13.1771 | -54.3093 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3191f4ce-9e5f-3661-ae0d-cd94b73b6425 | -13.18595 | -54.31806 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a784c7d-37ac-31e5-ba55-ea0966ada6c3 | -10.61922 | -54.74709 | 2026-10-09 05:06:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 69484870-317c-3e07-8994-27658bc98e04 | -13.17029 | -54.35191 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96e5472f-5602-360d-a5dc-aee0155f42c1 | -13.17695 | -54.35301 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 037fcd50-0fc2-37a1-a37b-8530630895cb | -11.90478 | -46.56398 | 2026-10-09 05:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 37db0564-c711-3139-b073-d9e303ef26ab | -11.78827 | -46.7993 | 2026-10-09 05:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f2a7713b-fa28-3b9e-a71b-df9b2860ed3f | -12.21942 | -57.10865 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8b77a2f5-e53e-3711-a990-02b428f24850 | -13.15201 | -54.33793 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c2930ff-1782-30ec-a5a2-227b83b5be98 | -13.40658 | -43.72717 | 2026-10-09 05:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9afa22a8-926b-32a3-93e6-fdd063d78c02 | -13.15973 | -54.3538 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| fea19368-05a8-3b74-9d5d-96a4365dfa58 | -14.94252 | -48.0984 | 2026-10-09 05:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e9a745f-2681-37b5-916a-02c8c29782d4 | -15.89052 | -46.46897 | 2026-10-09 05:06:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f646e6a5-6c32-3c2a-96f8-7a7a84819088 | -14.91498 | -48.07624 | 2026-10-09 05:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d001d389-3cb8-3ab5-a373-519d183b81fb | -13.36452 | -43.88456 | 2026-10-09 05:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de59a4d4-be40-30c6-af4c-ce523ed3204a | -13.16858 | -54.36257 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 925c0da0-4c1e-3911-8fa5-7a194f6bc160 | -12.21799 | -57.13917 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66786649-b9cc-3623-800c-7ebc166e74cb | -12.20417 | -57.13231 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 54a33be6-d116-3488-8b9b-6d8f50981779 | -11.8001 | -46.78056 | 2026-10-09 05:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d9a1ef5b-a8ae-3d57-9a9b-3a5709480b32 | -11.77005 | -58.27883 | 2026-10-09 05:06:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce33de43-7930-381c-94ac-9a998bee2893 | -16.53458 | -52.7445 | 2026-10-09 05:06:00 | NPP-375D | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5552c433-2a16-35f5-a325-5b4901800757 | -13.19523 | -54.367 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7681c1e4-7a0e-3bf4-9e09-8c0d4dfe3b63 | -12.23755 | -57.0899 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 37615391-e5dc-3ad0-b447-0afe12addc90 | -13.25087 | -42.24855 | 2026-10-09 05:06:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| e898a196-a73f-35f0-b908-55939aed92dc | -18.32455 | -42.3781 | 2026-10-09 05:06:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 5d542324-de10-3aa5-81e2-7cffda9f8ef6 | -12.21578 | -57.10802 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f9dfcb67-4cda-3f53-ba85-f8f4d2d05520 | -14.97513 | -47.54951 | 2026-10-09 05:06:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b3af6e1f-a91c-3a75-9dfc-8099ae3b2aa3 | -12.19146 | -48.41568 | 2026-10-09 05:06:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0c1be02-6f39-316b-95c3-3c885b9fed27 | -11.76257 | -46.78101 | 2026-10-09 05:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8660f17c-7308-3f39-8876-383dc4191a32 | -13.36406 | -43.88852 | 2026-10-09 05:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cde120a6-f7fb-31fb-8549-732d0679dc84 | -13.25044 | -42.25235 | 2026-10-09 05:06:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 851419e3-d9ff-30f8-9da4-7483cb639184 | -18.32573 | -42.36495 | 2026-10-09 05:06:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 71fb7295-c8f1-320b-a521-d3c5325e8364 | -18.33167 | -42.37357 | 2026-10-09 05:06:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| c6b9e623-ddf7-3e39-967b-726d15e81e82 | -13.15087 | -54.34503 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03ab66a8-f3e9-3981-95c1-2e71c2dec23d | -11.63106 | -54.54018 | 2026-10-09 05:06:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 463849b6-af65-33e7-9d88-a820bc028c67 | -15.78784 | -44.6811 | 2026-10-09 05:06:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f48ab0a6-5878-3959-ad7c-875def03b1b9 | -11.90943 | -46.56478 | 2026-10-09 05:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 27f39266-1276-3420-b998-108f5531ff62 | -12.25048 | -44.75145 | 2026-10-09 05:06:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9fe271df-2915-3a6b-b8cf-ff5767d29727 | -13.17914 | -54.36067 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 52bba204-f2d7-3ad7-a327-59e6a9803e9e | -12.29756 | -47.06007 | 2026-10-09 05:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3489d17-c0d3-3601-a616-7629e561196e | -12.47703 | -54.39865 | 2026-10-09 05:06:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31edd6b7-96fa-3199-9a09-0117fa9e820c | -9.2519 | -62.31103 | 2026-10-09 05:06:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c83c4f8-c2f8-30d3-bc2c-8a5ae47ac02f | -13.20969 | -54.36211 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4039014-b332-3d11-9030-9cf80fa2bf21 | -16.57605 | -51.62517 | 2026-10-09 05:06:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da5d0eed-3311-37dd-a113-1114b9016daf | -16.12985 | -43.75254 | 2026-10-09 05:06:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ec56031-6d5b-367b-a714-0c22bd81bb43 | -13.18913 | -54.36234 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 136a0c57-88b2-38ea-9cd8-ba241ee05a41 | -13.78663 | -52.79456 | 2026-10-09 05:06:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 050db9d9-678b-39dd-ac9f-be1eb03588e6 | -15.56657 | -44.51226 | 2026-10-09 05:06:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e2a62a0-044d-3e98-a26d-7cf62b541ae6 | -13.18247 | -54.36123 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| feb268d2-c328-3097-af85-d7a1c9a33011 | -13.16639 | -54.35491 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 03ebf934-5d84-38c4-96a4-ffa339b64a36 | -13.15761 | -54.32428 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07a7a950-ca42-3fd5-96b9-11c13f7548ab | -11.90412 | -46.56877 | 2026-10-09 05:06:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e7ebec2f-64c6-3fb4-8359-1211d01fc01e | -13.21245 | -54.36621 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11adb039-1268-3a0c-b4a4-c55b24a278b3 | -16.51348 | -52.58831 | 2026-10-09 05:06:00 | NPP-375D | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae2f3d28-b5ad-3073-93fd-8f9cbda4b307 | -15.21818 | -47.89963 | 2026-10-09 05:06:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cddcb25f-ec93-39f5-82cd-244a55604247 | -15.42916 | -43.24771 | 2026-10-09 05:06:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7f364940-cca4-3882-9f8d-0438d62b1a4d | -11.97885 | -57.61223 | 2026-10-09 05:06:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 849ab3f7-494e-37ee-a317-c6e91a4c84d7 | -12.21144 | -57.13361 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e5d8c7a-0c32-3a65-9683-74a68e4894a9 | -13.03311 | -46.81062 | 2026-10-09 05:06:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 51230011-c3a6-3fba-8e6e-466a768fcc09 | -11.97805 | -57.61682 | 2026-10-09 05:06:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 028ef54c-af74-3f0d-967d-4315e8748307 | -15.08378 | -43.11544 | 2026-10-09 05:06:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 7ac5c995-9a0d-3f17-8267-f0f7c72d3cc5 | -12.09553 | -57.15467 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6465a765-3a3b-3f92-8d41-433137a0dac9 | -13.15144 | -54.34148 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c63359d-bb37-3542-a9c5-b62fc635fd9e | -11.75353 | -61.0739 | 2026-10-09 05:06:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0104de3e-35f7-3c27-924c-e900ece153a6 | -13.16086 | -54.34669 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8dad1ce-ca08-37db-ad2a-173a8e27f75a | -12.2245 | -57.10071 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cd8d04f-970e-3b3e-9019-090636e46b1f | -12.09918 | -57.15532 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| accc1c24-a4ca-3bb1-bf5e-69f9064790d2 | -12.22303 | -57.0873 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 6e06936f-24ae-38f4-b315-5bb249676934 | -15.99887 | -53.69081 | 2026-10-09 05:06:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5bb6d80-73e0-3d12-9487-0e43a3131c4b | -13.20408 | -54.37577 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32b94036-4d46-3e67-baec-3e1fb38f138f | -17.17879 | -51.75014 | 2026-10-09 05:06:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4aa2e41c-7af0-33a7-abf4-41f99e7e7af0 | -13.16094 | -54.32484 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07404a34-37ce-31a3-8d3b-02e30d92a78b | -13.15924 | -54.33549 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f249ac2-71a6-3ff6-8712-dff0b2738550 | -11.96784 | -57.58696 | 2026-10-09 05:06:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b25a416-7000-3202-b874-731af8a2221b | -12.24408 | -57.09546 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f00e989a-4631-377b-a38e-4e45f31508d4 | -15.42966 | -43.24301 | 2026-10-09 05:06:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2b59aa20-3961-3ed3-ad6f-c823be10a638 | -13.16484 | -54.32184 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6974f555-ccaa-3bd6-954b-b0cf04999a12 | -13.16597 | -54.31474 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e235f820-86eb-3178-88ff-742c5095f1e0 | -11.74887 | -61.06489 | 2026-10-09 05:06:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6b0f794b-1cc6-39e2-8ba7-af1908c7142d | -14.17488 | -48.66439 | 2026-10-09 05:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0ad284dd-5c4d-3a9a-b4cd-6fe08b1991d6 | -15.07843 | -43.11401 | 2026-10-09 05:06:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 23.7 |
| d6a6b341-fd96-336c-ad24-47607bab938f | -12.1969 | -57.13101 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bfa48354-041f-35de-ad98-4425ac647636 | -12.21724 | -57.09945 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 595d395b-3e4a-301a-a9ac-42ecf130dffb | -11.50735 | -49.8979 | 2026-10-09 05:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27839f35-03e3-3dc0-ac39-bdf02ca76492 | -15.44662 | -45.44246 | 2026-10-09 05:06:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9a568ea-bb08-347f-b1b9-8ed15c2c8d9e | -12.21871 | -57.13492 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8f8fa3f-7bea-3ce6-9de4-7c4e2feff4e6 | -11.90685 | -46.5609 | 2026-10-09 05:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 77b4e8cd-8874-36e2-b887-b98118be18a8 | -13.17638 | -54.35656 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 456d0de8-c83f-3b04-93cf-f87a34225919 | -16.96094 | -46.35213 | 2026-10-09 05:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01c78c33-bb84-31e6-a3ce-504ed851817f | -15.5158 | -50.41089 | 2026-10-09 05:06:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8bb50a49-5e60-38ba-9707-b6966e366562 | -11.76323 | -46.77595 | 2026-10-09 05:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0bbea7c7-6542-31ba-bc3a-1c4bc76c2fa4 | -10.67496 | -58.73151 | 2026-10-09 05:06:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c7af024-e368-3a4b-8282-4f997e9a96f6 | -12.21578 | -57.08602 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 35.8 |
| ea80f589-6110-300d-bda3-31319046726a | -14.93416 | -48.09377 | 2026-10-09 05:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebf806dc-6a53-361b-b303-0e2d3aed8380 | -12.21796 | -57.09518 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| b3489385-9ffa-3650-8d0e-94ba08ca64ba | -12.21216 | -57.12936 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93d51c1c-d885-3852-88d3-f84ff0917077 | -13.17766 | -54.30576 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README173.md)
