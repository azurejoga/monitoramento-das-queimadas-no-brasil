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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fe7c914-c58f-3d30-8f15-81044a26152d | -11.19432 | -55.03321 | 2026-09-16 07:09:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b91c4942-db72-3319-942c-597d703a2ddd | -12.59943 | -50.7464 | 2026-09-16 07:09:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 720a696e-1e0b-327c-9b43-5a8282d0d69d | -5.14069 | -55.93253 | 2026-09-16 07:09:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 690eac52-4be1-378f-95f3-2d629d7a8a27 | -13.76398 | -48.81201 | 2026-09-16 07:09:00 | AQUA_M-M | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 25.9 |
| bf3a7496-fe53-3879-b787-0e3e69f0c878 | -11.79509 | -46.57558 | 2026-09-16 07:09:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 51749765-e4fe-3cd5-9cc4-e375b12af33c | -13.37788 | -57.02061 | 2026-09-16 07:09:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 33a44818-8454-37e4-9439-ab344df40655 | -12.618 | -50.76131 | 2026-09-16 07:09:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4fd1f3b9-0267-35ce-bd0b-c982843b86b0 | -12.60787 | -50.7599 | 2026-09-16 07:09:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 33d7e6c1-d433-3344-a682-02d51ee6e399 | -6.3256 | -62.6909 | 2026-09-16 07:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 2acda5c1-697d-3c8a-9861-3ea61f17151b | -12.6064 | -50.7691 | 2026-09-16 07:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| ae882c1f-ba5c-3311-846c-5aaa45c826fd | -12.6067 | -50.7476 | 2026-09-16 07:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 109.7 |
| e2149fbb-9dbb-3175-9672-158799db26e2 | -6.3257 | -62.6721 | 2026-09-16 07:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 7bb31417-15eb-3727-8a42-d1b32c4ce846 | -18.03087 | -50.94074 | 2026-09-16 07:12:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 94.9 |
| c189e7e7-0de9-3c31-b2e4-1dd301c63ebc | -18.02908 | -50.95522 | 2026-09-16 07:12:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 30.4 |
| be0ce0c2-34e7-31f8-ad0e-6c55f27aa2e4 | -18.02717 | -50.94793 | 2026-09-16 07:12:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 49d91c68-cfc5-35f9-9e48-e90991a81b93 | -18.02905 | -50.93357 | 2026-09-16 07:12:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 18916db5-269a-3a6a-b230-a2b553767ea3 | -12.6067 | -50.7476 | 2026-09-16 07:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 6ee744e3-de07-3ea8-90c0-931fcf708656 | -12.517 | -45.9205 | 2026-09-16 07:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 46e5f86b-9606-3c0b-87dc-f32646feaf3a | -12.4978 | -45.9235 | 2026-09-16 07:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 0560acea-a369-3096-a347-8bfeb77a6f0f | -12.517 | -45.9205 | 2026-09-16 07:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| ca2e23be-f0fe-3cba-975d-d0c3627fd89c | -12.6252 | -50.7882 | 2026-09-16 07:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 36.4 |
| cb199945-077c-3895-bed2-ac3a8c8e9ca7 | -12.6061 | -50.7905 | 2026-09-16 07:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 4df55bf9-9635-35de-a481-cb0c8136a7ef | -13.2239 | -51.6318 | 2026-09-16 08:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 62f840cd-013b-3928-86af-767f9652a6e3 | -12.6064 | -50.7691 | 2026-09-16 08:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| a0b8b8f9-0105-3bf3-8f42-5ed85b9ddade | -12.6255 | -50.7667 | 2026-09-16 08:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 36.9 |
| dcadb250-3bc4-3c61-bcb5-23b69d503107 | -12.6067 | -50.7476 | 2026-09-16 08:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 2e640ee2-3559-3ab7-ac65-f5c48ec1be67 | -13.2239 | -51.6318 | 2026-09-16 08:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| fb82dc90-9c90-3e77-bbcc-8f231df1394e | -12.5859 | -50.8572 | 2026-09-16 08:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 6e7ac3bf-7c03-3bc1-ba04-707ab3a536f7 | -13.2239 | -51.6318 | 2026-09-16 08:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 1b64cdae-28ff-3fcd-a80f-5a04c67c82df | -12.6057 | -50.812 | 2026-09-16 08:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 183811b6-a724-3516-a429-a2145d75d797 | -12.6064 | -50.7691 | 2026-09-16 08:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 5040121c-65e5-3c29-82b7-df6044ea1b3f | -12.6245 | -50.8311 | 2026-09-16 08:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 8a7c5582-39d6-346e-a8fb-ec0c495eb34e | -12.6628 | -50.8264 | 2026-09-16 08:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 47.6 |
| ae160fb4-731d-3e86-b0fb-988022c87fd5 | -12.6249 | -50.8096 | 2026-09-16 08:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 00909b37-83d3-3f60-8f2d-3b1428b43bcc | -12.5873 | -50.7714 | 2026-09-16 08:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 3cc7875f-29ac-3df2-9e27-80175623bc1c | -12.6054 | -50.8334 | 2026-09-16 08:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 54e28a87-88bf-3ff8-bce4-8637b241b830 | -12.6628 | -50.8264 | 2026-09-16 08:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 242286e3-b744-37bb-9ee8-fdceff707f00 | -12.58 | -50.83 | 2026-09-16 09:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3deaab9b-91cc-35ed-b73b-0528cec265c1 | -12.61 | -50.78 | 2026-09-16 09:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9d15fb48-b861-37ee-9826-a00c54e99910 | -12.57 | -50.77 | 2026-09-16 09:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8b0c187b-012d-3b97-aad4-8f1b798dfce5 | -12.61 | -50.84 | 2026-09-16 09:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7b1cc248-c35a-3bc5-bed3-ed7e8422a465 | -12.5869 | -50.7928 | 2026-09-16 09:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 200.0 |
| cf4524b7-3fc3-37bc-94a8-9033cc2ad6dc | -12.5873 | -50.7714 | 2026-09-16 09:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 27839c38-3d49-3725-bfa7-a0964da9753d | -12.5678 | -50.7952 | 2026-09-16 09:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 163.7 |
| 2337abd2-9824-3ca3-a1a6-8801d585aaaf | -12.5869 | -50.7928 | 2026-09-16 09:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 135.8 |
| f6ba953a-5e80-3094-a62f-bb88e1f96e50 | -12.6057 | -50.812 | 2026-09-16 09:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 60a35235-de1d-332a-9240-2646a16e04bd | -12.5866 | -50.8143 | 2026-09-16 09:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 6c2fb285-1c14-3026-80fe-82e70ed3130a | -12.5866 | -50.8143 | 2026-09-16 09:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 139.1 |
| dcfd9277-c7a1-389c-a7f6-84977502cbb2 | -12.5869 | -50.7928 | 2026-09-16 09:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 681c0d56-b478-3d6a-a438-9a9ddcaa2201 | -12.6057 | -50.812 | 2026-09-16 09:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 122.5 |
| e76ffb9a-027c-31dc-9bbe-0a1b53776dc1 | -12.5866 | -50.8143 | 2026-09-16 09:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 4487d46b-6bcc-3869-ba35-a5c652ad5fc0 | -12.5869 | -50.7928 | 2026-09-16 09:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 8eac4a9e-174e-3ae3-846e-67fa412f3ce3 | -12.5678 | -50.7952 | 2026-09-16 09:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 0027ea96-1b8d-3478-a9b7-9703826283a0 | -12.6057 | -50.812 | 2026-09-16 10:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 287.7 |
| 1a3d0709-db61-3600-9be0-92361b6f766c | -12.6054 | -50.8334 | 2026-09-16 10:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 82dcc1ed-79d8-329c-b095-be4189436589 | -12.5866 | -50.8143 | 2026-09-16 10:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 318.2 |
| 58197f93-7be1-3dea-b430-fd999b1de404 | -12.5863 | -50.8357 | 2026-09-16 10:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 90f59bb4-5e39-3e46-9d39-8263f2bf0bdb | -12.5675 | -50.8166 | 2026-09-16 10:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 116.8 |
| fe3d835f-6ce2-39be-be96-a85dade81086 | -10.1172 | -45.6118 | 2026-09-16 10:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| ed36bd30-40ab-37cf-9840-047a709b5b2f | -12.5678 | -50.7952 | 2026-09-16 10:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 167.7 |
| a2427f38-4881-353f-a0e6-99eb88b3babb | -12.5866 | -50.8143 | 2026-09-16 10:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 470.5 |
| a6e29a8a-ac62-3f05-8fe1-a421903673f7 | -12.5863 | -50.8357 | 2026-09-16 10:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 102.8 |
| bff81511-0dc5-320d-80ca-9102b18bf9d8 | -12.5869 | -50.7928 | 2026-09-16 10:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 1e4eccdf-060f-338d-8013-8984188ad160 | -12.6057 | -50.812 | 2026-09-16 10:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 150.3 |
| eecbcae5-f64e-3ade-87a9-0fd16c588473 | -12.5675 | -50.8166 | 2026-09-16 10:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 186.8 |
| b2dbde3b-6b9a-3720-b3b4-9b3f6b53acb9 | -12.5863 | -50.8357 | 2026-09-16 10:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 23509a8d-ab88-3f93-834c-8ae6ab7a9653 | -12.5866 | -50.8143 | 2026-09-16 10:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 490.0 |
| 2eb5928f-f0e9-3bf1-b875-c551ed5852f6 | -12.5869 | -50.7928 | 2026-09-16 10:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 7761646e-9658-36ff-9518-adaad7ef8e92 | -12.5866 | -50.8143 | 2026-09-16 10:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 344.4 |
| a9d7075f-dab6-3050-8e35-a9a660015e23 | -12.5869 | -50.7928 | 2026-09-16 10:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 6130db62-701a-3437-aabf-3bd2770b2470 | -12.5678 | -50.7952 | 2026-09-16 10:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 10feacee-98e5-3c0f-9da9-9174111faa22 | -12.6057 | -50.812 | 2026-09-16 10:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 181.0 |
| fd108884-db92-3c6c-99fe-375e09d5f838 | -12.5675 | -50.8166 | 2026-09-16 10:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 0203d266-c92b-37b6-abaa-4efe140ec3e5 | -12.5866 | -50.8143 | 2026-09-16 10:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 398.7 |
| f7fba3d6-ac84-3674-abbd-16322d42a051 | -12.5675 | -50.8166 | 2026-09-16 10:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 249.4 |
| bf13de9e-6065-311d-8710-c29dc7caaa07 | -12.5869 | -50.7928 | 2026-09-16 10:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 206.2 |
| 1a81a029-d088-3555-b095-d8d343ff28ec | -12.5678 | -50.7952 | 2026-09-16 10:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 206.5 |
| 88e09567-3691-304a-92c2-b39d3b7c7bf8 | -12.6057 | -50.812 | 2026-09-16 10:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 134.5 |
| a474346d-b38d-3d95-b1f3-bf515054363f | -12.5869 | -50.7928 | 2026-09-16 10:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 181.0 |
| aa65f6ba-b9bd-3fb4-b08f-c516eefdc06a | -12.5866 | -50.8143 | 2026-09-16 10:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 250.3 |
| f7577add-7e7f-3a4b-90c6-5031b9a8f5c1 | -12.5675 | -50.8166 | 2026-09-16 10:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 294.6 |
| 90119852-56d5-3a2d-bd22-b6a2c619620c | -12.5678 | -50.7952 | 2026-09-16 10:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 253.9 |
| 5c81db7f-41a3-3266-9b3a-430701dadf65 | -8.54799 | -44.51104 | 2026-09-16 11:06:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 27.2 |
| fd45a5e2-0b0d-380f-9a06-a9a0f1872a3f | -7.09024 | -42.09761 | 2026-09-16 11:06:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| d918216a-ca09-3a56-992e-f83711b957a1 | -7.79877 | -39.87312 | 2026-09-16 11:06:00 | TERRA_M-M | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 1690b2d5-9d6f-318f-b842-abfedd2d3196 | -8.55113 | -44.49118 | 2026-09-16 11:06:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 8d2978c3-1ec4-3789-a44c-13cd8d66d4e4 | -6.42464 | -38.53269 | 2026-09-16 11:06:00 | TERRA_M-M | POÇO DANTAS | PARAÍBA | Brasil | 2512036 | 25 | 33 | nan | nan | nan | Caatinga | 7.4 |
| a42cdd0d-07d7-314d-9fde-9ccdc3c2608c | -7.83168 | -37.53509 | 2026-09-16 11:06:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 571be943-3443-3af1-9f14-12df90e14027 | -7.04297 | -42.05008 | 2026-09-16 11:06:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 8e78a279-77a6-3634-96fd-d5d7134af4ca | -9.56478 | -37.33457 | 2026-09-16 11:06:00 | TERRA_M-M | SÃO JOSÉ DA TAPERA | ALAGOAS | Brasil | 2708402 | 27 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a9b6e481-56ef-31af-a2ad-9af8ff3839df | -5.89015 | -39.10456 | 2026-09-16 11:06:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 9024d4a8-6c49-385d-9b6a-52e287a31dd2 | -7.83295 | -37.52617 | 2026-09-16 11:06:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 131e35ec-8628-3fdd-8451-cadd787ddd09 | -4.34843 | -38.08907 | 2026-09-16 11:06:00 | TERRA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 7f97f00e-f95a-3ef3-9ce4-168d32734d28 | -8.5206 | -39.35086 | 2026-09-16 11:06:00 | TERRA_M-M | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 6319abea-9209-32e4-bc75-1f25e2f161fb | -7.03871 | -42.04366 | 2026-09-16 11:06:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 25.2 |
| 56f23006-e814-3788-b8c3-372579941e84 | -14.08715 | -41.20926 | 2026-09-16 11:08:00 | TERRA_M-M | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 2fe6b14b-67ab-34f7-ac54-ec31907e486a | -11.89529 | -43.81503 | 2026-09-16 11:08:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 944ab268-fcfe-3594-a076-1f4016e72549 | -10.06128 | -39.60486 | 2026-09-16 11:08:00 | TERRA_M-M | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 76e7c38c-c427-37d1-ba7e-b78a2e753d79 | -11.8293 | -39.18714 | 2026-09-16 11:08:00 | TERRA_M-M | CANDEAL | BAHIA | Brasil | 2906402 | 29 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 8e2a0dc1-691e-3a90-83a1-b8489e299b7e | -14.26006 | -42.39629 | 2026-09-16 11:08:00 | TERRA_M-M | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |


[Clique aqui para ver as próximas entradas](README68.md)
