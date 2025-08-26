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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 215f5213-4dc8-3f98-a775-7c4462145111 | -10.69611 | -55.14778 | 2025-08-26 04:46:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cc77c1f-bd75-3d55-b0b5-da395514f718 | -8.24415 | -61.45807 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 709acdc9-5232-32c1-a594-41a3d863f5a5 | -9.18436 | -59.50285 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59b4b754-10fd-3de2-ac1b-3fc23c9c8199 | -13.83452 | -46.69748 | 2025-08-26 04:46:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a2de56f-ac1d-3fe9-87bb-3a3075886f0c | -11.33898 | -47.8474 | 2025-08-26 04:46:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0c8e00d7-8d29-3911-b685-1a21f92af9f2 | -8.35135 | -62.9391 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 650ab6c2-732f-3b8e-b6c5-ff6ecf8cd7a0 | -10.4613 | -48.80334 | 2025-08-26 04:46:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6cf09b15-b10e-3b3f-886b-faedac0f8aa4 | -12.95191 | -46.32264 | 2025-08-26 04:46:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 538acb0d-8d2a-3519-aa48-fb67014ecd29 | -11.55075 | -51.88464 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a8aa1fd-fe64-3bd1-95a3-8fd4c6376af5 | -8.34527 | -62.93777 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a275cdbf-9a6d-3892-88f0-0b00485ee0e9 | -12.73432 | -48.1599 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 44f1619e-71e6-359a-95dc-795a51d07c5b | -9.23752 | -60.92262 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 983acad3-2f84-3988-bc30-787e1139a902 | -13.49256 | -46.87863 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bee97345-3c7e-301d-a8e3-43bb0ef48299 | -12.76368 | -48.1298 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1d4e61a8-4a99-311e-9fab-deb05667a49d | -8.57333 | -62.62967 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efaf4367-f4bd-3923-a1a7-c84c0c3bfa11 | -11.15327 | -44.76199 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 72aad416-3d0c-3a48-ad78-e53cd22d49a7 | -9.17762 | -59.5125 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d0fc3973-0fe1-3d79-8c10-1de23d12d839 | -9.23929 | -60.91278 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2588da3f-4a15-3354-b22c-3283b478d24a | -7.88814 | -63.0141 | 2025-08-26 04:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 563f50b9-f7eb-34cd-a44f-91f1fa8db024 | -7.88196 | -63.01288 | 2025-08-26 04:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 90e99c22-3050-3b7f-bde6-4ecf51e63796 | -9.15203 | -59.46787 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 79ff466e-9d53-3811-9f60-b59b5180cfa7 | -9.19397 | -59.53223 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0e558741-cb3c-3731-a984-487349c92208 | -9.76586 | -58.56031 | 2025-08-26 04:46:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14cf1189-20b7-3247-ac3d-da1ad98545dd | -9.57622 | -48.63012 | 2025-08-26 04:46:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae31cd55-592f-3028-8362-9d4ed7316e4a | -13.35633 | -51.79764 | 2025-08-26 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8cab7b8-fd8b-369a-b523-41b1346e60b6 | -9.27096 | -56.90709 | 2025-08-26 04:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9b6f592-63b2-347e-9d5e-768c1c345498 | -10.64205 | -51.59571 | 2025-08-26 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f398ab4a-a9a6-33f9-866a-fd912ff5dcdd | -6.81568 | -58.96198 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 08c7e63b-f880-3f95-bffc-b56baad6e8e2 | -9.61683 | -55.36286 | 2025-08-26 04:46:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1f4fc0f9-2548-372d-91fa-aedfac6889df | -9.16094 | -59.53023 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b12c27b0-d088-3bee-b2dc-063436ab3e0c | -8.992 | -65.40679 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 07551432-2947-3b84-a112-d3cb9c0914a7 | -6.90925 | -59.36562 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3fd00c2-f976-3e05-9546-0ab3ca8f622a | -9.00733 | -65.40285 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e63b2d72-1983-395d-87c9-59afcd367157 | -15.02512 | -48.50771 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 115933a4-4f2b-3692-a7e3-e8446a33c15c | -9.25568 | -65.62992 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7b9ba83-3961-3b9f-9331-ee30f2b72a9f | -7.47507 | -61.34927 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7df209a1-8ee3-352e-967e-13c495ebd724 | -12.56198 | -44.42463 | 2025-08-26 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 572c5711-da00-375b-bf14-ba306c3fb2f8 | -14.35925 | -51.9121 | 2025-08-26 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 29ef95a0-ccbb-3971-824e-c1884697a40f | -9.18048 | -59.52414 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 176bc006-ccf8-3903-a279-27361281be58 | -9.16873 | -59.54267 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0ccca3ee-1779-3337-8bf3-973f828cae43 | -13.39135 | -51.79221 | 2025-08-26 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8503c733-2b6e-30bf-8f02-483d9c9d5d1e | -14.71687 | -45.38533 | 2025-08-26 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 322ed0f4-d14d-3adb-ae14-47cd67930cb3 | -8.55124 | -62.64861 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 437d58e1-7995-3f99-9e75-2d28a06daae2 | -9.25881 | -56.90504 | 2025-08-26 04:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44545357-3ef1-35a0-926d-eacc3dcb7159 | -15.49484 | -47.88738 | 2025-08-26 04:46:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e51de3ca-7ee9-3dfb-ac97-56d0d3ee3dd7 | -9.17865 | -59.4525 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c6a3b37c-0fe0-37d8-89ee-86c9771f1930 | -9.18481 | -60.79308 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 753429c9-e5ef-38ba-b063-c0d5e49ecc93 | -13.52791 | -46.90406 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf5083a1-93b8-3da1-8399-3105086bfc08 | -12.75201 | -48.09175 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2236f241-f085-3b13-9e0f-3bf9df8337c1 | -10.10421 | -57.77055 | 2025-08-26 04:46:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61ae800b-b9e2-3dfd-bfd6-a4234acdc3f5 | -8.86193 | -62.45252 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1eab27c-6f31-317a-8c1f-3434c2b647e9 | -8.85101 | -62.44593 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 5f1a601b-33b9-30fa-b4a4-aa78e8feba37 | -13.06015 | -46.3164 | 2025-08-26 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0e142bc-beee-3977-b0a1-387a8c101fbd | -9.15777 | -59.46348 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb56ce3e-f448-3642-951d-d3f5684a2974 | -11.53599 | -52.13071 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a74a085d-1f60-3c7a-86e6-f68aaa81f717 | -13.48362 | -47.01013 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 50dfde19-682a-3c99-b058-2b2734b8e082 | -9.29657 | -48.42385 | 2025-08-26 04:46:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 168c0168-8f68-3f65-85b9-ce21baf17653 | -8.56139 | -62.62738 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd23bdd7-55ab-382d-9079-f2a6cb75113d | -8.86195 | -62.43022 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 144ae6dd-3ee0-31a2-b242-285cdf5c4a0e | -11.34219 | -47.8525 | 2025-08-26 04:46:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7dd59a67-7828-3b04-adab-78c960ff892d | -7.88383 | -63.01134 | 2025-08-26 04:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2e98543a-3c15-3c6f-8bf2-b37bd07425c6 | -10.85952 | -47.33905 | 2025-08-26 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fa96bc0-45d3-3bf7-ae9d-d166beb1cef6 | -13.38579 | -51.78397 | 2025-08-26 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3866d67-38f3-3045-9a43-af08f625c427 | -8.63314 | -62.65296 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e246464-9b8c-3d7b-8641-7ac3efae01db | -8.23866 | -61.45657 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e7298da-9586-3179-834b-cd85d7ce0058 | -9.14904 | -60.78451 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b37414a3-4b07-38f5-92d8-650b3e5d04b9 | -13.62794 | -48.15032 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 409be354-a922-3222-a8c2-79fc5ad9b038 | -8.84787 | -62.44069 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 46aa1d4a-6366-32bf-b613-20aef51fbbca | -9.18541 | -60.78988 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b1a7f0b-8a3f-3f70-8740-80c5aac43be4 | -7.44086 | -60.62125 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 650ee0e5-60db-3c5c-a824-38485e3bb980 | -13.4456 | -47.00716 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e53779ea-cdc4-384d-a881-72f39b0dc53a | -11.54262 | -52.13179 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b47b56a2-6ae0-35c0-b074-08fa9e527d0e | -9.56535 | -55.37664 | 2025-08-26 04:46:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0e633263-05da-3011-843b-81bf6a75bf5c | -11.54372 | -52.12477 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| efa5d51d-76bc-32fd-8f85-69abaed5be39 | -13.66307 | -46.89101 | 2025-08-26 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58d8e289-8ec0-38c0-8129-c9840cf97fed | -8.30778 | -55.09513 | 2025-08-26 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0720071a-5f62-3d64-8471-ad4b5b0b7149 | -10.43801 | -47.18064 | 2025-08-26 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 97115938-067c-3990-8143-0553b5fdfb98 | -9.17637 | -59.52746 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d8f18b7-08ee-37c1-9b66-0e02a6141827 | -7.04827 | -59.19773 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 591ef8e3-ed03-3b60-afb2-229aa73267bb | -11.56083 | -52.10233 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b276450a-fe78-3eff-81ef-001f0277c4ff | -12.7571 | -48.14892 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a6c29498-21ba-3058-8177-33a8eb779b0c | -9.47296 | -57.82359 | 2025-08-26 04:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5eb46172-557e-3524-a937-d2ab192918bd | -16.31957 | -43.62002 | 2025-08-26 04:46:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b972b53c-b4fc-33bf-a38d-5ce942dedbe4 | -11.56138 | -52.12042 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24a9ee1f-d7fa-3066-a822-b91b5bb9c67e | -9.19687 | -59.51623 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f450f754-1822-30e5-849a-d4599495e678 | -15.1377 | -48.67259 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9ae404e6-74e3-3ad8-a5fd-04e13e811d40 | -7.38848 | -64.35847 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f0985d5d-d58e-36b5-9d0f-e4e72244c774 | -11.57076 | -52.12554 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| d9d5650b-4233-33a3-b827-b1ea67ee92b3 | -13.50418 | -46.8884 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70986467-201c-3e96-a068-6a3ba1b9ec7f | -11.54908 | -51.87355 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a19fa72-f430-3f86-a6dd-e0dc12c9f84d | -15.02124 | -48.50705 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 213d3a99-acc0-3b9d-b8ba-7a1ea122de29 | -11.54178 | -50.45483 | 2025-08-26 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04688d2f-1df8-3f6a-9dc1-bbbe3f7419be | -10.87549 | -55.79555 | 2025-08-26 04:46:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1f374798-bff4-35ab-b659-76f66748715f | -9.56608 | -55.37235 | 2025-08-26 04:46:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| eeb639d7-3177-372c-8681-2783aa9444ed | -8.57762 | -62.63991 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed99e088-864f-3e7a-9024-c0585c83d799 | -11.62789 | -46.21017 | 2025-08-26 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 724a3634-aecb-315d-b93e-c2c10793aaea | -9.02799 | -65.73785 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6240f77-d192-3925-adf2-2c27570cfa6d | -11.63783 | -44.86339 | 2025-08-26 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fce9eac-806f-3570-a5cf-221eb56bc051 | -9.18643 | -59.44147 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3aa0d356-21e1-3fd0-bf86-ba6041cf779e | -13.35577 | -51.80124 | 2025-08-26 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README71.md)
