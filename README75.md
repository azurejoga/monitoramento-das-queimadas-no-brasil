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
| eb763c35-1441-3ad7-88db-2f3e0007bca5 | -15.99873 | -50.94733 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7732993c-cc95-3cca-bb8f-c86feaf887e0 | -13.25968 | -48.05719 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b096d92-7244-31f3-a0d3-b4f611308bf0 | -16.29511 | -50.99435 | 2025-10-07 04:38:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 646376d4-c843-3b21-946f-3012e30218c4 | -13.02938 | -51.03242 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2838000f-490b-35bc-b15f-5d7dc2893784 | -11.29344 | -49.99261 | 2025-10-07 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4b54c08-cbbd-3031-8813-00652239abbb | -14.62497 | -52.49188 | 2025-10-07 04:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eaac5201-f254-37bc-b73e-1b5bf736aad1 | -16.04519 | -50.96624 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1920bd90-9dba-3fd2-9b55-1fd72e950032 | -10.41592 | -50.30599 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| ae752e25-c2b5-3634-8d32-77579c169307 | -14.28707 | -45.84958 | 2025-10-07 04:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf5ee2da-b83e-3360-bc6d-2d76e7d587fa | -10.4535 | -50.35369 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e5cbd2e7-792c-3d04-96bf-9c7aee5637e0 | -10.49807 | -51.49512 | 2025-10-07 04:38:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e513e1b-6b7e-3cc7-8022-e70be10a2897 | -14.76833 | -46.03646 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a0907e15-7581-3a9b-887c-bcc7382b2312 | -15.22544 | -49.31182 | 2025-10-07 04:38:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7ecad85-195d-3f60-bf53-85884dff0773 | -13.37196 | -47.23786 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 94d5c339-deb6-3688-8dad-b0957d55fed2 | -11.67423 | -46.33912 | 2025-10-07 04:38:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af03e948-41d2-313b-9200-79f43dd1310d | -10.60143 | -49.63712 | 2025-10-07 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53a02b4f-2840-3b06-a61c-850761e9a61b | -16.04441 | -50.99227 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c5275a4c-1129-3e85-901a-ac0dfacbd4b2 | -15.51216 | -46.83338 | 2025-10-07 04:38:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33712bb5-38de-3caa-b706-270ad14c8232 | -13.10725 | -47.8217 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e062c1b-1d2b-3900-ba73-2a3ca5e5fee9 | -14.91159 | -51.44461 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| baadc95c-6655-3e94-8062-fc6a96127ffd | -13.27113 | -47.19169 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 463b21a1-f749-3975-b547-3f1d9d201d87 | -10.42252 | -50.32968 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a448de2b-56dc-32b1-90a2-f1f89de5486e | -13.7124 | -48.08158 | 2025-10-07 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27b52a22-163d-3067-8d0d-10ba1b8fbf63 | -13.7855 | -45.78386 | 2025-10-07 04:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e67495d8-2ed0-3fc6-9380-1fd14f1ef84a | -14.92301 | -46.79912 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 642b8d23-630a-382a-b8fb-8f8bc6840cba | -11.02599 | -50.91448 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 907729f0-5a03-3cb4-b409-a62efa0edd37 | -12.25164 | -47.85278 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae000cc5-124a-351a-8428-3a5322928e62 | -12.34414 | -47.05779 | 2025-10-07 04:38:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb05330b-9fa7-3675-b501-7c8bd4b8d33b | -13.65345 | -48.73437 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a6936e5-5294-33cd-8839-9d04bf66bb05 | -15.39458 | -48.0103 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a7b979af-5c2c-38e5-8a57-d62dfa2259a0 | -10.40554 | -50.32685 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 14ec3340-6f1b-3cf2-93df-626f177615ce | -14.91608 | -46.81644 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81d84cac-e53f-3f34-ac52-4e852d747906 | -10.42435 | -51.63195 | 2025-10-07 04:38:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71d67dfc-491f-3fa5-ba76-e02557083e82 | -11.21109 | -54.98328 | 2025-10-07 04:38:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc41b913-bceb-3d54-87fc-8bd116cbcaf6 | -10.8814 | -51.0269 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 456c82ac-50e4-3a88-9bc8-db916ee8ba91 | -13.28698 | -47.80762 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ede9907f-f99e-3820-8955-0a9770e4ed14 | -14.76459 | -46.03591 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 969c8bd2-0be6-37b2-84b4-014b40425380 | -14.73595 | -46.02222 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4626504f-8953-35da-a34c-91c89819befd | -14.49928 | -46.92749 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ab422a5-b485-36d2-b842-9b6da8ddfda4 | -14.79123 | -51.37051 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 52f7b571-4e66-319b-a99f-f27c498af2bc | -11.73908 | -43.29459 | 2025-10-07 04:38:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 46c821e3-9917-3369-bf33-10d200587bb9 | -13.3205 | -47.7708 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc0d1078-0b98-34a0-9d08-71a371d9f749 | -15.58612 | -52.55415 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fad47edf-1d05-3d31-916d-a1e4d7f27f90 | -11.84237 | -44.91347 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ccb2b7a-a1cf-31c0-a8ce-106c8c2adf79 | -11.84932 | -44.9197 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c09557b7-cb07-3819-aea9-a5bd4ecb02a2 | -15.36096 | -47.30641 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f29694da-9dcd-3f64-b8f2-82273a1713e8 | -13.26249 | -48.06152 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03f1e561-c476-3c4a-8cce-54525ebbe6b2 | -14.93133 | -51.40957 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a27fac9d-5935-36ad-942b-426100cba0dd | -12.02367 | -49.71658 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 963166a4-0940-3bbd-a04a-f8995512e709 | -15.80757 | -43.67379 | 2025-10-07 04:38:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2dfae006-f413-371d-97ff-44b0235477fb | -16.29526 | -45.24247 | 2025-10-07 04:38:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea65100d-f5b2-361e-bafd-c143c94aed21 | -16.29126 | -45.24191 | 2025-10-07 04:38:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23c3bfe5-b8f6-3d87-9ad2-601b19af4e89 | -10.11039 | -58.5281 | 2025-10-07 04:38:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cfe28161-9c27-3c90-a0a5-77b435dc052e | -11.12286 | -47.76036 | 2025-10-07 04:38:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 293af097-8b82-3df7-9070-7ecf4660edc6 | -10.45377 | -51.23898 | 2025-10-07 04:38:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dde5b082-2868-36e5-8567-2582971ca85b | -15.27314 | -46.34979 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6b9e429-aba8-3e9e-ad64-9fec15cefebf | -14.64802 | -48.37104 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 64f9ead2-db05-313e-9684-9250a99732b2 | -11.65004 | -47.75611 | 2025-10-07 04:38:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e898afe5-6510-30e7-bdb7-eaf0fe4dcfc2 | -13.09026 | -47.86471 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6818451a-f86a-3180-ac46-b6824ea2afbf | -15.97107 | -50.84189 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0b2febd-fdc3-3ab7-9444-19e1c1d84a8a | -15.97083 | -49.10788 | 2025-10-07 04:38:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 651ed6a1-d6ae-3a48-a85f-9cd3593934fb | -15.5158 | -46.83381 | 2025-10-07 04:38:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e4540fe-e5d4-3c78-b26c-d851f31083e7 | -17.56186 | -46.07643 | 2025-10-07 04:38:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63996d75-e7d0-31d5-87f3-9a28b2c5ba3b | -11.78258 | -48.91632 | 2025-10-07 04:38:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 01384181-da90-3c66-809b-ee895ba2671a | -11.06392 | -49.55973 | 2025-10-07 04:38:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4b318ac5-30b2-36ae-a7ff-293e615c9c15 | -14.28332 | -45.84899 | 2025-10-07 04:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c5ad79cb-f5c2-32c6-8e1b-701da42ecffc | -10.9447 | -51.17189 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef8ecac2-2f50-3bd5-86bb-811bbe4b4ab0 | -14.91064 | -46.82844 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 64e2d7c5-cc71-30bf-b773-a13c0935113a | -10.25489 | -57.92032 | 2025-10-07 04:38:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dce51bce-b79a-3170-b7c5-fb609509791f | -11.15489 | -47.75428 | 2025-10-07 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6575f96b-9369-3f3f-84c1-386cad8b65b6 | -17.56357 | -50.44604 | 2025-10-07 04:38:00 | NPP-375D | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 519be079-e7f5-3aa9-8340-9f530f5dd87c | -16.06898 | -47.77424 | 2025-10-07 04:38:00 | NPP-375D | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9e07c78-1979-38e2-9684-4d1bedb672ac | -15.5777 | -52.56116 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3bcb9bd0-21f3-3c53-a2fb-c36a777314c9 | -11.7439 | -43.29119 | 2025-10-07 04:38:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fc0dcdb2-8859-3b91-9334-a062ac081c6f | -14.70804 | -48.38846 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce997670-2e54-3b3e-9ffc-057cd0a28909 | -12.25717 | -55.11031 | 2025-10-07 04:38:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79d9b99d-ca9d-3def-8e0e-dda560158dc1 | -13.38074 | -47.53484 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa27f0da-51a6-3e82-9590-f868610d8951 | -10.42092 | -50.31811 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63fec8c8-3e00-3be4-aeef-c10d379be647 | -10.42711 | -50.3229 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| c185b26e-0cc7-3f02-a8cb-4713e87fd5c9 | -10.4255 | -50.31134 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 92e639b4-e18c-3f8f-93d3-f819472c016b | -16.008 | -50.82585 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| afc72fc9-791e-3bc5-ba10-d7630604f4f2 | -12.38846 | -51.08389 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b123515c-72e8-32c5-92ca-685d83ff7319 | -13.67444 | -47.33445 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 317576a9-a74f-30ee-96e9-cd67f5e31abb | -13.33098 | -47.24429 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 026f2153-974e-3115-834c-4c62b6f44e46 | -13.33306 | -47.75715 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| bc1b1f28-4869-3326-a1f8-ddf7e6250823 | -13.2563 | -48.05661 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 96809847-3fb6-330d-a071-efc453006557 | -10.45728 | -51.23949 | 2025-10-07 04:38:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f77518d8-3a6f-3166-9ae3-30e328772523 | -13.94885 | -48.17589 | 2025-10-07 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 523e1daf-1712-3f89-9ccd-b41e7dad0cd3 | -15.56112 | -52.44666 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3bc3944e-8019-3676-b563-96e2337fc898 | -11.86098 | -44.93425 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d09cc2a-089d-3b3d-bff6-14ec84a6cedb | -12.13555 | -50.8761 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d51c2b3b-9082-3b89-9d00-8f4b263ff97c | -13.24857 | -47.17533 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 22200ae0-8d2c-3110-956b-0bf949b9222b | -17.71893 | -40.246 | 2025-10-07 04:38:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e67ac8d6-4712-3412-b025-81e6e71ef000 | -11.84401 | -47.60149 | 2025-10-07 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d130c391-f26b-304c-80e3-9d0bf9122091 | -13.71971 | -48.19298 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f05b75ab-5924-30df-b600-4340faee1984 | -14.92057 | -46.81636 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7fc06a2f-0bf1-3bdf-bdc5-2bc0597d8269 | -10.74819 | -50.47362 | 2025-10-07 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 628ccca4-44bc-31bf-b18f-2421b5f1060a | -12.38504 | -51.08331 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ed75269-cfc1-3b84-84c4-1523ed555833 | -15.44588 | -51.55475 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75886530-1214-35a6-9d6d-b7602bbb0537 | -14.80744 | -44.89375 | 2025-10-07 04:38:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README76.md)
