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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b26ad91-4a6b-32be-88f7-4fae062a5599 | -8.18529 | -49.58624 | 2025-09-06 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53e9391d-2716-34fc-b07f-84568aa9e5df | -5.75057 | -43.70463 | 2025-09-06 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cafa787e-35fe-35b0-8e9a-d57be9c26e55 | -13.32653 | -51.72394 | 2025-09-06 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d592e015-7a84-3520-9573-8a5f7736ebb5 | -6.15987 | -43.17298 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 50a21786-f425-3a93-87f9-5a1d47a9648c | -5.75486 | -43.1264 | 2025-09-06 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f8b3cbd1-19fc-3a51-b843-d24d0b2c610a | -13.9006 | -48.02343 | 2025-09-06 04:17:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 436357bd-2d26-3e3f-bbb2-1b4032dcf001 | -14.80319 | -48.12038 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 824eb056-218b-3a33-a07f-f849717ed0d0 | -3.37876 | -47.61123 | 2025-09-06 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d57dede-8b0c-3d14-a660-1da9bcdeee80 | -3.36099 | -43.37497 | 2025-09-06 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11c755c2-8c96-3695-b2a6-df62efa909f4 | -6.07769 | -43.35172 | 2025-09-06 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5f3710a-4b0e-36d3-9d9d-0cab0cd2ac10 | -12.87593 | -48.00343 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c8985b0-7122-3810-b846-0c1b1777b588 | -5.68982 | -48.13408 | 2025-09-06 04:17:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8bbdd310-cd1f-3860-8921-143875b4f131 | -13.27144 | -46.81193 | 2025-09-06 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13eb5295-a554-3b59-b33e-5dabdb19c459 | -4.80145 | -47.26374 | 2025-09-06 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d5dc88e-ad19-3a57-8a49-c21240509c29 | -6.61362 | -43.98238 | 2025-09-06 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e6d0ab09-0fb4-385e-bad3-f2f646e5f578 | -14.26494 | -52.1897 | 2025-09-06 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23d34e60-4f5d-39fd-9ff3-d86be1b82742 | -6.27462 | -53.42938 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60a793e5-78f0-33f7-8092-0786582db16e | -5.95509 | -53.80119 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7f14653d-3ab7-3686-b7a3-c462070c4069 | -6.5961 | -44.5546 | 2025-09-06 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0d4d778c-c561-38ce-82e9-de7cb63a7df3 | -6.2652 | -53.44855 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6611b414-40f0-3bba-9c57-e79748e650c2 | -4.50411 | -42.88277 | 2025-09-06 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 139b3651-f59a-3234-8379-f8198c60d9cd | -13.56346 | -48.11691 | 2025-09-06 04:17:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 933243f7-810e-3f7b-8e52-ecb2c81ef46c | -5.95913 | -43.03065 | 2025-09-06 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4ac029f4-e32a-3826-84eb-26d8d9d7ca3c | -7.25735 | -41.89177 | 2025-09-06 04:17:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1d676b81-19a1-3bec-a15a-cbef7cd55196 | -10.06639 | -48.07861 | 2025-09-06 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1fed12b-442c-3e27-907d-cfdcd61e9d58 | -12.84952 | -48.0031 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cb819fe-8819-30d8-ac87-f94bc6aa81e9 | -7.04416 | -44.35324 | 2025-09-06 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b466aea8-c759-3e0d-8796-8517cb5b565f | -8.93322 | -48.64937 | 2025-09-06 04:17:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef6d0adb-2c80-3548-8daa-7443dc567149 | -5.99616 | -49.23184 | 2025-09-06 04:17:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d84befbb-04a2-3458-85e5-cbf9e5d54860 | -13.38761 | -44.58406 | 2025-09-06 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 87679ee9-58fc-3856-acc0-3a9b60173fa8 | -6.48267 | -43.97561 | 2025-09-06 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3f74fc8-97f0-395f-adb7-f21b3bd71ff1 | -5.67754 | -43.57096 | 2025-09-06 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 270ce6fd-42ca-3575-a054-4c93622e1b2a | -6.91572 | -44.1685 | 2025-09-06 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46e62588-5e7c-35df-abd4-419ea2b6f0f1 | -17.00822 | -43.78334 | 2025-09-06 04:17:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 06f1b9ee-6a47-317c-a1f5-3ca8266b8dab | -9.05447 | -50.45596 | 2025-09-06 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a2845f8b-86a1-3aeb-8822-2d26b4ce8d31 | -6.55163 | -42.94259 | 2025-09-06 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a589e99a-24d6-3450-9f98-84e7caa50df7 | -12.94844 | -54.79945 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea209835-0cb2-3e57-9319-059bcca5046f | -5.22607 | -43.27779 | 2025-09-06 04:17:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bdde7ce-213f-361b-a7bf-60111e43aa64 | -5.63061 | -44.99499 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17abde15-ac8a-3a03-8ac6-02305f42a511 | -6.33661 | -43.5536 | 2025-09-06 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b34513f6-385a-33ed-8c5f-a1ef171af430 | -7.34563 | -43.95102 | 2025-09-06 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 44f9e32e-fb27-3bbb-80a0-3c1466c10535 | -6.54295 | -49.50764 | 2025-09-06 04:17:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 91e7778b-733f-3439-b8d8-1812c04dafd0 | -5.6742 | -43.57043 | 2025-09-06 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b259c716-9208-3fd5-85de-808c9e303d03 | -5.67734 | -45.17392 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1024cd66-9474-3726-b241-90359c3de1e0 | -7.98304 | -44.51043 | 2025-09-06 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e271d446-d0c5-3cfb-9cc1-cc3008b51ade | -6.15654 | -43.17246 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d834ad8b-d2eb-3121-afb6-08a1a37762d9 | -12.61981 | -56.99062 | 2025-09-06 04:17:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 270fb8a4-3bdc-3b9b-b720-b9bf30c7f28b | -5.96646 | -53.59614 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af423d2f-8300-30b2-82b6-d1e452bde4d3 | -6.0688 | -43.34318 | 2025-09-06 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5cb90cfc-b1be-3e3f-983a-3e8aad2599d9 | -6.10612 | -48.10261 | 2025-09-06 04:17:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a382c1a-fc49-34a1-89bc-d0db8aed6cf0 | -6.15269 | -43.19675 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0dbbee45-e471-3dd8-9de4-80198a14950a | -5.96259 | -44.13025 | 2025-09-06 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4975fa47-eed7-3797-95cb-d1cec3adcd4a | -5.94779 | -45.66119 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94670203-e4d3-3fc9-9149-f845fa7817b4 | -14.45409 | -47.27928 | 2025-09-06 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3713c9cf-d33c-3eb1-be73-a5759b7ea94a | -7.6845 | -50.29161 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 71bfec6f-a462-315d-8b5b-e04b35a9e19b | -5.12984 | -43.0772 | 2025-09-06 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92427d95-19f1-3752-ad21-6df082c39006 | -13.06364 | -47.10413 | 2025-09-06 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5805a0f-0a2a-3a54-9f18-315850f90779 | -13.60244 | -43.12416 | 2025-09-06 04:17:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 64de16d1-a7b1-319b-9ecc-0ff159b09a54 | -10.09449 | -46.23901 | 2025-09-06 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 930a8447-8b9b-3af5-a4d5-6c90503eda47 | -14.57141 | -48.01264 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f9f9b06-f4af-323c-9fc0-9c4cfa6d3893 | -5.93473 | -43.01259 | 2025-09-06 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9416f422-9afd-3fb5-a382-a51d06638af5 | -5.03313 | -49.75735 | 2025-09-06 04:17:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3743395f-1feb-3912-ac29-b609dbaa6c82 | -15.18539 | -47.98961 | 2025-09-06 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45cf2b18-f8c4-3405-920c-f09fd5b955ca | -6.51661 | -42.41286 | 2025-09-06 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 48aca92a-7da4-3c03-b294-cd422e74b995 | -12.18802 | -53.90096 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5f3c451-d290-3835-9eb0-49d5b8952225 | -12.6198 | -56.98508 | 2025-09-06 04:17:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 395f3212-4381-36b4-9367-1beac71ffe35 | -5.97235 | -53.5972 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00a3be35-30a3-32d3-8a47-2b1677fc697a | -6.16487 | -43.18444 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8b349428-343f-3594-b34d-f5ce2e204c48 | -12.98836 | -48.05032 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2091bd1e-ee5b-3dab-84fa-e6deb0985e69 | -9.08667 | -46.99623 | 2025-09-06 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2f70b257-bcba-3da2-8e96-c5f769294d87 | -5.98786 | -44.72885 | 2025-09-06 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d50c310-6d19-3618-8e84-9e3143c37321 | -14.56416 | -48.01165 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 16e05ea5-1be1-308c-a2cc-16805719feb1 | -7.34619 | -43.94751 | 2025-09-06 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9318ed5a-d698-38fb-b11f-825f9c6d70c6 | -6.01628 | -43.69626 | 2025-09-06 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f12c4bf2-6ada-3635-bd5c-b80f6efe6b06 | -12.48463 | -53.85644 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0524b21-09e9-3f27-b7f4-ad1a44491ef7 | -6.50939 | -42.41532 | 2025-09-06 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f448c9a4-cb18-3eec-8ce7-0fbba3b0b34c | -15.18255 | -47.98477 | 2025-09-06 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4dfa930-6806-3255-8516-b22e87191c64 | -6.16432 | -43.18791 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cf6f82f8-1654-3fcc-8ad6-2bf2db66f8a0 | -13.8538 | -46.29296 | 2025-09-06 04:17:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 429b35fd-1d29-36d4-9e77-1b933d485947 | -12.89971 | -48.01553 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b96733dc-3d04-37e4-bfbf-993247563880 | -5.84648 | -45.30792 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a865cd04-a0ff-3751-8ae9-3adcf88bfef9 | -5.73138 | -43.91122 | 2025-09-06 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bd74024-2815-358f-9ef7-6d01eee3fdc4 | -6.32952 | -44.9537 | 2025-09-06 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43a487bb-a7d9-37d5-a0af-506341adb754 | -12.4918 | -53.8596 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39ecbb80-a968-36e2-a8df-232d9152eed2 | -8.05273 | -52.37539 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e9ff0921-b092-3d62-b77d-bcc53f98583d | -5.98504 | -44.72459 | 2025-09-06 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| eabc6064-2183-3047-8774-7356dc977334 | -5.87036 | -52.1711 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc836213-f7be-3c0c-a793-2ce8d5f00f06 | -6.2121 | -44.72581 | 2025-09-06 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10a6520b-298c-3897-860c-251a56e5869f | -7.07815 | -43.86924 | 2025-09-06 04:17:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| edbbc4ab-2534-38f3-9cfb-887f7b7ba13c | -14.43164 | -48.43836 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b28f6c9b-c890-34c7-9f48-6f6c144103a1 | -4.50689 | -42.88676 | 2025-09-06 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a1c0dbf3-4f90-3149-a180-4ad79cb20197 | -5.62654 | -44.99816 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18eb1900-4955-399e-93ba-7c9c4e731fb0 | -16.9209 | -45.74779 | 2025-09-06 04:17:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11f65d24-95b4-3684-a5ee-277f87e15f1c | -12.19339 | -53.90218 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba9227f3-cea0-3a0c-8dd9-5f6bb3e37411 | -4.86301 | -50.82943 | 2025-09-06 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| af1c8617-3aa5-3a9e-a6e9-4cd32e3c393e | -5.72888 | -45.36499 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2388b75-97d1-3bc5-afd0-6a300af85247 | -5.8506 | -45.30459 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48fd553d-db2d-30d0-8b54-b284a5e1ecfb | -9.70858 | -49.49371 | 2025-09-06 04:17:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| bc1f89d1-3740-3568-bbad-591d95c602bf | -6.21399 | -43.36289 | 2025-09-06 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 694e0665-4895-3a74-b29e-4a9d58396899 | -6.40792 | -44.46514 | 2025-09-06 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README46.md)
