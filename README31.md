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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 638c9266-ed04-338d-b81c-721253628baa | -13.0639 | -48.46269 | 2025-10-30 04:06:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9019a78-360c-36d6-a2d2-96f733db5230 | -12.81699 | -43.45208 | 2025-10-30 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4ee8a25-9639-302b-bcda-2495e842be8e | -9.71443 | -43.37806 | 2025-10-30 04:06:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 10d6cfff-2bb3-3a1e-805e-6953979587bc | -9.86049 | -47.69578 | 2025-10-30 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dad28948-36c6-3929-961f-2174c69ac22c | -14.22858 | -44.31815 | 2025-10-30 04:06:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 358019c9-7c8f-3c50-896c-d22ec1430ce0 | -13.3267 | -47.47655 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a5d5da7-dc02-32a4-beca-0e68dfc441c7 | -10.27568 | -48.0576 | 2025-10-30 04:06:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9308c861-7d58-382b-b2dc-533dd31eeea5 | -12.36182 | -50.15315 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dd5350b3-3b33-3713-85ca-247862d92aeb | -13.47391 | -47.99988 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 843c9a9c-3aa3-3c26-bd5a-f3d9ef60f803 | -11.84961 | -47.92888 | 2025-10-30 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3f64a72-f41e-315d-a306-8c6306f9ae60 | -11.87078 | -46.7568 | 2025-10-30 04:06:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b32eea7d-50d7-3083-a242-f238a2d50d1f | -8.7911 | -42.82764 | 2025-10-30 04:06:00 | NPP-375D | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4d460359-ccd0-3f33-9d02-6a5574a6b3de | -13.31693 | -47.482 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d9274b61-645e-366c-a56a-d655f76652c4 | -12.81228 | -43.45912 | 2025-10-30 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 01727f35-e7d6-38ee-aa3d-6534b6dce353 | -12.39987 | -46.82486 | 2025-10-30 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 167b0343-3f70-36eb-8f1e-36463a52ac28 | -13.27235 | -47.74745 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4fc9546b-6cce-32b7-bbcc-a3213b630abd | -13.41935 | -47.37435 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5d1ff93-f05e-3866-abe1-3b5a508b7cf0 | -10.48904 | -45.04153 | 2025-10-30 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c3275262-fed1-3e80-82e2-3060399f4c77 | -12.83827 | -43.45183 | 2025-10-30 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cd149f0-ad8d-3969-b118-79f378f4a27c | -12.22486 | -46.47188 | 2025-10-30 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ce425d39-9c0e-3bee-bb70-1e426119d659 | -13.3442 | -47.67105 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ab78b1d-53eb-3983-8099-ff146d320cb3 | -12.47914 | -50.581 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2ade5432-1013-33eb-b90f-826a250181f3 | -14.68807 | -43.15117 | 2025-10-30 04:06:00 | NPP-375D | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 82556274-f12a-368b-8029-b24a854516e9 | -12.49749 | -50.57096 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 136efda6-8f2c-32fd-859b-b47cf4ce6c4b | -12.18626 | -46.71259 | 2025-10-30 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d0c7f096-3bcc-3c27-8331-445742a47de4 | -13.52861 | -47.12973 | 2025-10-30 04:06:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb424faf-b93b-3d6f-97c5-6544b34937bb | -10.33254 | -47.09232 | 2025-10-30 04:06:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b47cd32-89e1-3a3c-815e-0f7931bec833 | -12.29546 | -50.27111 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 833a34d3-2733-3fe8-8fe7-254e30eb336e | -9.49644 | -40.37659 | 2025-10-30 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 07eb6076-e007-3bea-a513-360a6c938128 | -10.35756 | -47.28051 | 2025-10-30 04:06:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| dd0eba05-1f91-391a-be70-e1b1a64ac484 | -14.48441 | -43.13911 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d29cb980-0e6c-3963-97e4-97e825e25d89 | -14.5738 | -41.14548 | 2025-10-30 04:06:00 | NPP-375D | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5017ae39-abaf-3824-8c9b-ed26c86b4381 | -10.95697 | -50.22369 | 2025-10-30 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86afb3a7-bb0f-34e6-b487-35a869de1c51 | -13.52753 | -44.34196 | 2025-10-30 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2bdade1f-a473-3c28-84cc-0aa5cea06a64 | -11.63984 | -44.04518 | 2025-10-30 04:06:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 19d12e78-ab13-3628-b7d5-ffa5570f80ce | -12.94734 | -46.53624 | 2025-10-30 04:06:00 | NPP-375D | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 982a709c-e08c-3608-84c1-a3f482d09a34 | -9.81578 | -44.72897 | 2025-10-30 04:06:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 252cf901-043f-3d98-8089-4a950cfc47b3 | -10.97768 | -50.22084 | 2025-10-30 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 166a2748-71e6-3529-bb81-89caa7b07005 | -14.28957 | -42.34045 | 2025-10-30 04:06:00 | NPP-375D | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 68170609-6e40-383e-b7d3-87e2e3f63948 | -10.39366 | -48.28036 | 2025-10-30 04:06:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c858a224-a5df-3a5e-ab70-d30a02a4252f | -11.80236 | -42.84352 | 2025-10-30 04:06:00 | NPP-375D | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 99fd2696-ced5-356f-8e1d-1fc255fb8486 | -10.91558 | -47.81174 | 2025-10-30 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e9bf43a-4928-33f2-b090-b0b1a0e38114 | -10.34937 | -44.07312 | 2025-10-30 04:06:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d24b614-8088-3858-8e3a-e0cbf452a2c1 | -9.23946 | -45.56303 | 2025-10-30 04:06:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9d3811c-8f5b-31a8-8900-fca0ad242763 | -12.16314 | -46.56627 | 2025-10-30 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 345980e5-1703-337d-a5f9-fbb5c33a2ced | -12.83075 | -43.45446 | 2025-10-30 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61c4ddc0-728f-3a4a-aed9-4bbd113eca0d | -8.32653 | -47.93322 | 2025-10-30 04:06:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 1a089c12-1dcc-313d-b9df-0f2dea88da97 | -10.74063 | -44.74941 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f4841ecb-1c29-3569-b418-ed6b7fc42c4b | -13.5726 | -47.15382 | 2025-10-30 04:06:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 50c85fd0-5ee7-30f5-a8b6-8c83ddbd171f | -11.96067 | -43.28738 | 2025-10-30 04:06:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 088ac7c4-38b8-333b-8d13-b28b1a924633 | -13.71777 | -48.77057 | 2025-10-30 04:06:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b54de330-e636-3e69-8935-987d1046c248 | -12.70872 | -46.30323 | 2025-10-30 04:06:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e144e661-67d7-3dd1-b26e-cf4e3125ec2f | -11.06837 | -47.53933 | 2025-10-30 04:06:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a6e1ed46-96a9-36c8-8e3a-9ba0883c4be7 | -9.22408 | -45.60416 | 2025-10-30 04:06:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0a2685f-49ef-3492-9890-a1c12bfc7b89 | -12.48505 | -50.57875 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e84f2ef-e15a-37f1-99e6-97b6dbd19916 | -10.25267 | -43.95864 | 2025-10-30 04:06:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 783ab46f-256a-38de-ad34-a0273a990f7a | -12.77676 | -43.10461 | 2025-10-30 04:06:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5c8b1af4-e10e-3dfb-a9be-cccbcd5e4973 | -7.95791 | -46.71296 | 2025-10-30 04:06:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea71bec7-22dd-37ab-bf31-eb1d2e1f9f54 | -12.28686 | -50.31595 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6234380-27be-35a5-a111-66070875f758 | -10.76565 | -47.88838 | 2025-10-30 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1166851-5192-3121-9d6e-018053eabd27 | -12.58316 | -44.95584 | 2025-10-30 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 27308d62-09d0-3e0b-bedd-94751b5484a9 | -9.65882 | -44.55961 | 2025-10-30 04:06:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcb736c0-b41d-3917-a4ae-bc25dee2c8fb | -13.04116 | -48.45852 | 2025-10-30 04:06:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5d27a2e3-2460-322e-abb9-63fdc02e251e | -12.83419 | -43.45506 | 2025-10-30 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 461801ac-bcc1-3c53-979d-9ac8310d454e | -13.81793 | -41.69562 | 2025-10-30 04:06:00 | NPP-375D | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7d297bb3-4ca0-39fc-a9ef-0fbe98df8784 | -12.36589 | -50.15419 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e1d84a1b-229b-3302-857d-8844d872a576 | -11.95273 | -49.94252 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c4e789d-83a7-3458-b04e-6fdce3ddcd69 | -9.50031 | -40.37362 | 2025-10-30 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 446ed9db-b147-3ece-9484-36db03b3a514 | -12.16245 | -46.56271 | 2025-10-30 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82fd7030-7061-31f3-a8e6-a8d9df4d8177 | -13.42491 | -47.36747 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8486f13-825e-31c6-a565-c35ea20c0c62 | -12.30125 | -50.26898 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e40bd7f-68a1-31bf-809a-8c9eb16a5bdc | -14.23949 | -44.27491 | 2025-10-30 04:06:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c307c7de-2d98-3b5e-90a2-773878d64119 | -10.51788 | -40.32983 | 2025-10-30 04:06:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3b966fd9-1a02-3655-b100-76e22081d595 | -13.17638 | -48.43816 | 2025-10-30 04:06:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b63167a-69b6-3d12-81a5-ea79ef47aa42 | -7.79435 | -48.3057 | 2025-10-30 04:06:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17b237c9-9ddf-3394-aec1-bcc83a4622b5 | -13.5535 | -47.13372 | 2025-10-30 04:06:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16fd6fe1-6115-32ae-8db3-7286b1cd27e3 | -10.44937 | -44.32115 | 2025-10-30 04:06:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42303367-dcea-3acd-b226-1d24b04fc242 | -12.68503 | -46.298 | 2025-10-30 04:06:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b7d5befa-4b45-3c52-b001-0ead3ed1a1be | -12.5181 | -50.5678 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8d13f1a5-955f-3940-80b2-31719bbf06e6 | -12.51283 | -50.56673 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e4d85e75-026d-3364-933a-8e8285a3fa60 | -10.74072 | -44.75147 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35a78838-63ff-36bd-a16d-7c9c66c5c2a3 | -12.31267 | -48.06714 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b99fd943-078d-39c7-969e-9153615f7a01 | -14.36536 | -43.56346 | 2025-10-30 04:06:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d409105-aa09-365c-94ce-227a52d91073 | -13.57451 | -47.33076 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dda46272-71c8-3cdd-aac2-7e56e9b6db24 | -10.85705 | -47.87642 | 2025-10-30 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a2e8cc5e-40c0-3b2c-a68e-7731a04545f8 | -12.50991 | -50.56318 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1e7d7a30-cf16-3ab3-a36f-18264f04a44f | -12.88478 | -48.63762 | 2025-10-30 04:06:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea3a7fe0-0026-3aa2-b72d-2bd640b92bb7 | -11.91566 | -44.17484 | 2025-10-30 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b5aeabcc-9cbd-3ec8-8977-c7a769b7c5b5 | -10.86178 | -47.61369 | 2025-10-30 04:06:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0818433d-1292-3201-b902-f08e60f32a52 | -10.08164 | -43.88458 | 2025-10-30 04:06:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 135e9971-087e-3e2b-8920-98ed927b4c17 | -14.30472 | -44.52958 | 2025-10-30 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3d2cd9b-5e8d-30f3-8ce7-044202a73ed0 | -13.38469 | -48.50742 | 2025-10-30 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66f5d2a6-37a7-3e7c-a19a-9837c7f50b54 | -10.98085 | -50.11875 | 2025-10-30 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8cba34c-5f05-307d-adff-79379c7c59d6 | -12.47387 | -50.57991 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9ed92310-83c1-380c-88f8-8177e5d45064 | -12.29276 | -48.07471 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7e03a74a-f951-317b-8595-d25fc7a53883 | -10.74136 | -44.74506 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 95266c7f-2cb2-3d4e-b86b-7459c94b19ae | -11.81859 | -42.80811 | 2025-10-30 04:06:00 | NPP-375D | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1298c9d2-21cd-3695-9830-0f56e239e6b3 | -13.30214 | -47.0659 | 2025-10-30 04:06:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7c4d00b-75ab-357f-b930-ef33f3531935 | -12.50338 | -50.56872 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f22ae316-3e8e-34e9-b96a-7791e2ba6cd5 | -10.49543 | -44.13578 | 2025-10-30 04:06:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README32.md)
