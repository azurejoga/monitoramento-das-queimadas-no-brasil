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

## Dados Diários - Página 230

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13fa5a43-c509-3aa5-a5ea-14803b1d5007 | -7.65514 | -42.53514 | 2024-10-09 12:00:00 | TERRA_M-T | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 56.9 |
| ae9c2e59-593a-31d8-ab54-18276ccda9aa | -11.01719 | -41.16005 | 2024-10-09 12:02:00 | TERRA_M-T | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 9ab8ecfc-688a-3abd-883b-7c6f0192364d | -11.21696 | -41.43369 | 2024-10-09 12:02:00 | TERRA_M-T | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 288d90e2-fec8-373b-a8b8-860ea9b9f859 | -10.38576 | -40.68836 | 2024-10-09 12:02:00 | TERRA_M-T | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 12.3 |
| be28f430-3c77-3177-a1b6-93eb880b0b94 | -10.92393 | -41.02964 | 2024-10-09 12:02:00 | TERRA_M-T | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 035fe87e-cc49-35a0-b194-0a1aa114a946 | -10.99434 | -40.39365 | 2024-10-09 12:02:00 | TERRA_M-T | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 40652555-bfae-3cbc-9d7f-7f240845dc10 | -11.01507 | -41.17342 | 2024-10-09 12:02:00 | TERRA_M-T | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 15.8 |
| e873e794-01eb-3888-ad7f-e77edb3bf4a9 | -10.3838 | -40.70113 | 2024-10-09 12:02:00 | TERRA_M-T | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 12624e55-1e99-34dc-a8c0-5f22567cafdd | -10.2928 | -40.28666 | 2024-10-09 12:02:00 | TERRA_M-T | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 5b84e929-a981-3a4a-ac49-549d33293e60 | -10.19818 | -39.43309 | 2024-10-09 12:02:00 | TERRA_M-T | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 30.5 |
| 41bce368-5162-3f96-af5d-26d3587507dc | -11.78267 | -44.5289 | 2024-10-09 12:02:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 6942631a-0b37-336f-a3af-be7d002882f1 | -11.7887 | -44.53629 | 2024-10-09 12:02:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 95874259-9490-35de-842c-6a02abe5b65f | -11.79279 | -44.5129 | 2024-10-09 12:02:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 69959378-1b9b-3154-ad9a-4d3aeadccd3b | -11.7964 | -44.53127 | 2024-10-09 12:02:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 00b86b0c-94c0-3867-9d96-8b48f4b46030 | -11.96609 | -45.16177 | 2024-10-09 12:02:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 727ffa67-0d81-354d-a3aa-34cb26060624 | -11.96788 | -45.16902 | 2024-10-09 12:02:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 5ceb8192-39e2-3554-9d4f-33660c4bef66 | -13.92702 | -44.52243 | 2024-10-09 12:02:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| f1760953-5019-33b9-9fd6-bf24a3e4da32 | -13.93996 | -44.50972 | 2024-10-09 12:02:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 607.1 |
| d24c7396-b2c2-38b8-9807-ca3a57e68668 | -13.94938 | -44.5334 | 2024-10-09 12:02:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 9865c90a-c610-375f-80e8-aa2a48857414 | -12.16991 | -42.44684 | 2024-10-09 12:02:00 | TERRA_M-T | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 19.3 |
| f3c66285-d08e-3d24-bd76-e85b9d7d0227 | -11.77496 | -44.53394 | 2024-10-09 12:02:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 39.7 |
| c27fbefc-dd28-3a44-93fe-a357a01bf4e2 | -11.51195 | -41.45834 | 2024-10-09 12:02:00 | TERRA_M-T | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 21.1 |
| f0795f1d-5aa9-3e7e-95ab-7da36c06a55e | -11.51746 | -43.99506 | 2024-10-09 12:02:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 424dd111-c4e2-356a-ab56-b5bd67004070 | -11.65748 | -42.68308 | 2024-10-09 12:02:00 | TERRA_M-T | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 45.5 |
| 2aa68820-233a-318e-b765-9985da2c491b | -11.67773 | -42.63449 | 2024-10-09 12:02:00 | TERRA_M-T | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 17.3 |
| d287060d-3578-39ad-ab90-b3f7164ccb6b | -11.6805 | -42.6178 | 2024-10-09 12:02:00 | TERRA_M-T | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 36.5 |
| 5b50a422-a66e-3e15-b27f-b032bd7d79ab | -12.31403 | -42.61772 | 2024-10-09 12:02:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 8be18988-4058-32a8-8931-ad2ad52de7c6 | -12.3257 | -42.6197 | 2024-10-09 12:02:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 19.2 |
| badd0783-9866-3341-9429-c60bb4c549d6 | -12.62429 | -41.70034 | 2024-10-09 12:02:00 | TERRA_M-T | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 0b5ae31a-f1e7-37bb-b361-6b89f79faedc | -12.62642 | -41.68687 | 2024-10-09 12:02:00 | TERRA_M-T | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 18.2 |
| d24cf908-f81e-3757-8bdd-94a5dfdf3791 | -12.62901 | -41.69296 | 2024-10-09 12:02:00 | TERRA_M-T | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 29.6 |
| 5aa90ee5-1477-3121-9c38-1460ecd90431 | -12.63295 | -42.36387 | 2024-10-09 12:02:00 | TERRA_M-T | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 18.5 |
| a4468188-3735-3a14-a132-def8b3dae8f8 | -12.64405 | -42.15784 | 2024-10-09 12:02:00 | TERRA_M-T | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 68fad723-aea4-380d-b2cc-fd6d15fec682 | -12.73889 | -42.06819 | 2024-10-09 12:02:00 | TERRA_M-T | NOVO HORIZONTE | BAHIA | Brasil | 2923035 | 29 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 8f5cc61b-e731-3a50-8593-59a73e6ffb7c | -12.79343 | -41.72641 | 2024-10-09 12:02:00 | TERRA_M-T | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 33.2 |
| 1ed04c9d-de1b-3e28-b043-06f9ceda7334 | -12.80933 | -42.34296 | 2024-10-09 12:02:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 29.8 |
| 66afa4aa-bd3a-37a6-954b-0a2374097328 | -13.41853 | -40.42574 | 2024-10-09 12:02:00 | TERRA_M-T | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 84667aa6-70e7-3070-be0a-e453792818fa | -13.61184 | -40.9529 | 2024-10-09 12:02:00 | TERRA_M-T | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 41.0 |
| 69fd22f2-cc69-3ff4-9ed4-f5a0ba321e40 | -13.61373 | -40.94103 | 2024-10-09 12:02:00 | TERRA_M-T | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 24.5 |
| 16b484d8-a05b-333b-ba11-db9bafb6eaad | -13.70516 | -42.22575 | 2024-10-09 12:02:00 | TERRA_M-T | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 46.9 |
| 50996d0e-6529-3b01-8345-6538f6ce0d31 | -13.70753 | -42.21119 | 2024-10-09 12:02:00 | TERRA_M-T | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 24.9 |
| f95ed3d9-b685-36ad-896b-4888f865ec07 | -13.89018 | -42.71236 | 2024-10-09 12:02:00 | TERRA_M-T | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 19.6 |
| d8c40fc6-aef9-3203-9a60-56c13c805cef | -13.95275 | -41.83686 | 2024-10-09 12:02:00 | TERRA_M-T | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 82bf8c09-5112-32d8-a727-a04905b96b36 | -13.9826 | -43.40963 | 2024-10-09 12:02:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 700c2531-2318-37d2-b83e-6bf9db708c72 | -13.98554 | -43.39202 | 2024-10-09 12:02:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 90c40d19-625d-35af-bb7b-36ee2032ffa6 | -14.11075 | -40.71809 | 2024-10-09 12:02:00 | TERRA_M-T | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 5096aaa4-cb6e-3690-ad81-005a3e66082a | -14.11658 | -41.32517 | 2024-10-09 12:02:00 | TERRA_M-T | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 9d05f52e-44cb-395d-aeff-ccbdeb4adee4 | -14.11857 | -41.31276 | 2024-10-09 12:02:00 | TERRA_M-T | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 19.0 |
| ad92aa8c-b8b9-332f-9651-b21b11859188 | -14.12095 | -44.97358 | 2024-10-09 12:02:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| c9cae2bf-cfba-3f1a-b4f2-b879d8f592e3 | -14.21489 | -40.83584 | 2024-10-09 12:02:00 | TERRA_M-T | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 880427c6-5dfe-3cef-90e5-f4ae0435fe04 | -14.21673 | -40.8241 | 2024-10-09 12:02:00 | TERRA_M-T | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 46ed5300-09c9-3e4d-846c-eb084b355f7f | -14.23421 | -41.29872 | 2024-10-09 12:02:00 | TERRA_M-T | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 53.8 |
| 36d2605a-4104-313c-9030-d7ea1714c910 | -14.26218 | -42.06756 | 2024-10-09 12:02:00 | TERRA_M-T | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 7a0d1876-f882-3f56-803e-df5d55d23192 | -14.29048 | -42.03008 | 2024-10-09 12:02:00 | TERRA_M-T | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 03512ae6-21e7-3016-8c2a-7b47c3ef10a5 | -14.35281 | -42.35216 | 2024-10-09 12:02:00 | TERRA_M-T | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 7c5767c6-2949-391a-87c6-8255150bca14 | -14.35514 | -41.76473 | 2024-10-09 12:02:00 | TERRA_M-T | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 7f8c874b-56c0-3f71-8aa4-c5879f8ad5a7 | -14.62292 | -42.25547 | 2024-10-09 12:02:00 | TERRA_M-T | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 0889a89b-b2b8-3b6a-a126-e8403ddc2dac | -14.74382 | -41.57499 | 2024-10-09 12:02:00 | TERRA_M-T | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 36.8 |
| c23e2798-c148-317f-8658-3452ca7e2d64 | -14.8173 | -46.63577 | 2024-10-09 12:02:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 41475d60-e77a-3491-b894-c19908982445 | -14.84123 | -41.28113 | 2024-10-09 12:02:00 | TERRA_M-T | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| ab9dddc0-c292-3e1d-9e8c-c81b98ce691e | -14.90943 | -40.39842 | 2024-10-09 12:02:00 | TERRA_M-T | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 3574993f-9a47-37fb-b37f-270d3ee39bad | -14.92271 | -41.41351 | 2024-10-09 12:02:00 | TERRA_M-T | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 93432d82-e2a2-348f-8fe6-7f18c3ae357a | -14.93354 | -42.40622 | 2024-10-09 12:02:00 | TERRA_M-T | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 12.9 |
| f8333314-3282-3d26-821e-e180d77318ac | -14.96847 | -41.96629 | 2024-10-09 12:02:00 | TERRA_M-T | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| a37122aa-6bb6-3761-a317-921554136dd5 | -15.41956 | -43.78522 | 2024-10-09 12:02:00 | TERRA_M-T | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 7eb58268-187f-390b-9cc2-c7dc03158771 | -15.59017 | -40.70298 | 2024-10-09 12:02:00 | TERRA_M-T | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 541a6c66-a048-3628-88ab-35d5711f6d6e | -15.79464 | -44.67886 | 2024-10-09 12:02:00 | TERRA_M-T | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 37c558ad-199a-3f68-94c8-09470a7adacb | -15.81339 | -43.49124 | 2024-10-09 12:02:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 2e904e25-d36f-37f8-96aa-d655237d85c6 | -16.21713 | -42.86863 | 2024-10-09 12:02:00 | TERRA_M-T | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5374a353-2061-3554-83e4-117d45133cf2 | -16.53483 | -42.28369 | 2024-10-09 12:02:00 | TERRA_M-T | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| eed70463-31e1-3ed4-b15c-3ffbb2dc76cf | -16.75501 | -40.65007 | 2024-10-09 12:02:00 | TERRA_M-T | FELISBURGO | MINAS GERAIS | Brasil | 3125606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| bd5cec26-ff88-31b6-a62a-f6b403d7cf3b | -11.27129 | -41.37217 | 2024-10-09 12:02:00 | TERRA_M-T | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 2f4befdb-8f24-3853-9552-456bee791ed6 | -9.6946 | -42.77412 | 2024-10-09 12:02:00 | TERRA_M-T | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 42b9e75e-4d1b-35fb-bdc5-5fd8679b091e | -9.69283 | -42.76764 | 2024-10-09 12:02:00 | TERRA_M-T | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 35.0 |
| 1c0cba6d-1741-3b62-bff0-baf566cdd675 | -10.79937 | -42.44563 | 2024-10-09 12:02:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 54.1 |
| 923a5a3f-eae2-3ff3-97c8-aa603eacc2fd | -16.96 | -57.46 | 2024-10-09 12:03:49 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0caf7b18-44d1-3878-89f1-e8267fcfbc98 | -21.2179 | -44.22582 | 2024-10-09 12:04:00 | TERRA_M-T | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 132.7 |
| 5df8c07b-226e-38e3-b43d-7e6ae6a71f8f | -17.09858 | -41.3398 | 2024-10-09 12:04:00 | TERRA_M-T | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| a563d685-fbb1-3e3b-bdd5-7a4f2c237198 | -17.10047 | -41.32782 | 2024-10-09 12:04:00 | TERRA_M-T | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.2 |
| d9e42238-d909-3964-8a8f-78e05f026296 | -17.30059 | -39.36526 | 2024-10-09 12:04:00 | TERRA_M-T | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 30.3 |
| 746b8c0e-ed8e-3507-8c80-8fb4092ac4a5 | -17.31579 | -41.83856 | 2024-10-09 12:04:00 | TERRA_M-T | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.7 |
| 70d571d9-1c2c-3162-89b6-d207ee7f874e | -17.31597 | -41.8444 | 2024-10-09 12:04:00 | TERRA_M-T | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 45.1 |
| fce36d3d-a488-3dce-be15-b37fe9056503 | -17.31791 | -41.83217 | 2024-10-09 12:04:00 | TERRA_M-T | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 7872d5cb-ba7b-3c43-a19c-2a6736b60fa0 | -17.32593 | -41.8401 | 2024-10-09 12:04:00 | TERRA_M-T | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 4d1018ec-34c1-3727-b580-546e6c391901 | -17.34237 | -44.87033 | 2024-10-09 12:04:00 | TERRA_M-T | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 22.9 |
| e122494b-adb3-37cd-898e-089b1e14fb12 | -17.3726 | -44.92482 | 2024-10-09 12:04:00 | TERRA_M-T | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 22.7 |
| ae0e83f7-8e7a-38e6-afb2-cfc13863bf3a | -17.37623 | -44.90458 | 2024-10-09 12:04:00 | TERRA_M-T | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 711b862b-a279-3752-97a8-8daabe9e829f | -17.41769 | -44.89164 | 2024-10-09 12:04:00 | TERRA_M-T | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 32.5 |
| bc8fb807-9557-37bd-aaea-f69740170c41 | -17.53796 | -40.64444 | 2024-10-09 12:04:00 | TERRA_M-T | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| e35c992f-4701-32fc-b2ae-f997df0fabea | -17.53958 | -40.63412 | 2024-10-09 12:04:00 | TERRA_M-T | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 430fa517-cce1-3747-b8d3-33ea055a8a6f | -17.55516 | -40.65798 | 2024-10-09 12:04:00 | TERRA_M-T | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 2614702b-bf26-31a9-93d7-3159cdf3e910 | -17.89531 | -41.42859 | 2024-10-09 12:04:00 | TERRA_M-T | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| ce5183b3-0b53-377f-9db6-a55ff7a1693c | -17.90593 | -40.11871 | 2024-10-09 12:04:00 | TERRA_M-T | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| c736e0ab-16b7-3e01-88ad-a0f8cdad531e | -18.00824 | -42.13326 | 2024-10-09 12:04:00 | TERRA_M-T | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| f68613c8-2c62-3bae-8f2e-12064a74e477 | -18.63089 | -41.11119 | 2024-10-09 12:04:00 | TERRA_M-T | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 4cc0cbac-10d1-3783-b217-1312545d0214 | -18.63433 | -41.11791 | 2024-10-09 12:04:00 | TERRA_M-T | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 7974d578-3da6-370d-9e00-0e0b6bfc6085 | -18.7803 | -43.08702 | 2024-10-09 12:04:00 | TERRA_M-T | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| d03ee9d1-2efd-3b08-8585-fbd256bee139 | -18.84227 | -43.11312 | 2024-10-09 12:04:00 | TERRA_M-T | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 8550e51b-ec59-387b-8629-166c212df174 | -18.84452 | -43.09961 | 2024-10-09 12:04:00 | TERRA_M-T | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| d553c6b6-fb92-3146-98e8-6b33120818bc | -18.85526 | -43.10154 | 2024-10-09 12:04:00 | TERRA_M-T | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.7 |


[Clique aqui para ver as próximas entradas](README231.md)
