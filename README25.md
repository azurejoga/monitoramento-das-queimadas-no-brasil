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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85b3fb2b-498e-32bc-af1b-38a7c2bec499 | -13.36113 | -47.29438 | 2025-09-29 03:49:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a180d0f-ebd6-3ccb-ada4-76779c030420 | -14.58675 | -45.02588 | 2025-09-29 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 29357141-73b4-3897-b54d-b28526ffa869 | -19.67772 | -43.77373 | 2025-09-29 03:49:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94a40c7d-0ae3-3bf8-b4a3-1459beb84da1 | -19.87203 | -43.80538 | 2025-09-29 03:49:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 97ad2e2d-3e67-34a6-aa5f-013bc7faee4a | -14.56777 | -48.26357 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64247015-c24e-3888-956f-704de06de67f | -14.59201 | -44.99887 | 2025-09-29 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df6c406e-aa57-3d04-a150-dc69af0057b6 | -14.40564 | -41.28878 | 2025-09-29 03:49:00 | NPP-375D | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d1785708-adfc-3811-a4e7-a09156dfa8b7 | -13.76269 | -47.91528 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7ca1984-cae8-30dc-b481-81bfd5716838 | -14.57674 | -48.2798 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 012e1426-f96a-35da-a4a1-2c0df287fd48 | -15.03637 | -46.9682 | 2025-09-29 03:49:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a66cb03c-bff8-3671-9bd8-5b90c066969c | -14.54188 | -48.44525 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ee4c182d-27b4-360c-a51d-c17de10b55f3 | -12.91528 | -47.15763 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 205a4729-b475-3a87-a4b1-e94201adaba0 | -13.82859 | -47.49751 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e68e5e4-6932-3a25-ab72-2181005f030f | -12.76031 | -46.85231 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16c30f34-6e55-37ef-a13e-fb56e6121e5c | -14.57639 | -48.24118 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86973fcd-4dd6-36e5-a33a-e3a218c681d2 | -14.57048 | -48.23988 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a52896a6-24ef-3a9d-8e7f-a4b6b8212424 | -13.03207 | -49.45658 | 2025-09-29 03:49:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd27c360-bb52-3d05-b185-8bb27c973ca9 | -15.40251 | -44.9834 | 2025-09-29 03:49:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39692a32-20b8-3a83-9a4a-0146cbb9f79c | -12.9655 | -46.24177 | 2025-09-29 03:49:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3620ba4-3aa5-3774-9278-13174aef1eac | -12.85702 | -46.96898 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| edeb3b25-5d24-335b-8697-0de377506508 | -14.56704 | -48.25673 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bbd4943d-6914-3c79-bcca-107a804a8cf5 | -15.58545 | -41.81194 | 2025-09-29 03:49:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 905e1182-22df-324f-9540-750226e734dc | -19.85582 | -43.80182 | 2025-09-29 03:49:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e26e81b1-3fbe-3c1a-9ebe-6fbe32e8466b | -14.63008 | -48.2915 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f16a525b-c301-39db-b413-37f16c7cc393 | -25.06092 | -49.35811 | 2025-09-29 03:49:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4c4f330f-2275-36a8-bc68-b3e5e47ff8ff | -14.48894 | -48.54645 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b19d124-3af2-39df-8831-d777a9b874ad | -20.63271 | -43.95611 | 2025-09-29 03:49:00 | NPP-375D | SÃO BRÁS DO SUAÇUÍ | MINAS GERAIS | Brasil | 3160900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fcaeaa85-1c46-3832-a25c-16bd49e27c59 | -13.76657 | -47.91136 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54a3ecd3-dcdb-34b2-9f64-822eab6961e5 | -12.7589 | -46.85947 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1cc0fb93-cba5-364e-a2d9-d10bb83d65d5 | -13.63265 | -47.31121 | 2025-09-29 03:49:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6403b471-18d9-3a4d-8e71-395cc8421dc9 | -13.83159 | -47.48253 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca6e74ef-60a7-3dfc-902d-fabddfdeea72 | -13.79009 | -47.88684 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93458d5d-5799-3f7b-b5a2-292a099f619b | -13.80356 | -47.91073 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 18a7930c-4ca1-3969-8225-37153a985dee | -19.67841 | -43.77001 | 2025-09-29 03:49:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57a0de23-dddd-3acf-906f-b421e185572f | -14.56796 | -48.25225 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c995f7a7-a67d-311a-b80f-b4dbe85b7bf1 | -20.56916 | -41.94074 | 2025-09-29 03:49:00 | NPP-375D | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| eb814851-4942-362b-bb7f-1c9d3384f7e6 | -13.78748 | -47.86987 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a330bc26-fb7e-3d18-9011-8d52c3ec620f | -15.05891 | -42.34127 | 2025-09-29 03:49:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 19.4 |
| b7ce7c09-83bd-3adc-9451-10aeb2fcce38 | -15.04739 | -46.96825 | 2025-09-29 03:49:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c155a1d0-215e-37d1-9595-a7f498a44684 | -15.05245 | -46.97257 | 2025-09-29 03:49:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3c608b71-7a0f-3120-b44e-ee633d32241e | -13.79414 | -47.89687 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 71da84a2-f3ba-3588-b15e-fbefd4c9cdbd | -13.0 | -49.43566 | 2025-09-29 03:49:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3b92f42-df4b-3336-b8c3-9d68f6a04905 | -15.02873 | -46.97681 | 2025-09-29 03:49:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8229cf6f-98c0-3986-a8c3-a7c51c7ae06d | -14.79407 | -45.73179 | 2025-09-29 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9fb7ed3-cfea-32ef-bafe-3b2626bea2e2 | -13.7666 | -47.9264 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c7e5a8c-1e28-3169-a20d-a27bcc5ebcaf | -13.7431 | -47.89072 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 826ab890-bc2d-3dad-9d19-1ebbfe300340 | -13.54572 | -44.17157 | 2025-09-29 03:49:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94a79f87-53a5-3d4c-ba9d-00b47557cbb0 | -12.80215 | -47.75509 | 2025-09-29 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c928482b-e798-3dce-9de8-090657b6b998 | -12.76459 | -46.86025 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a09edab-0187-3d6e-b64e-c088955bca07 | -14.52717 | -48.4213 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e8346b6-4828-3c87-8da6-792a86018ff5 | -14.54976 | -48.40788 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d7cc770-da4c-30f3-9679-30ce1241fee1 | -21.41873 | -43.89487 | 2025-09-29 03:49:00 | NPP-375D | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 17b353f8-42ea-386c-84be-aecf05634aec | -14.56123 | -48.25489 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50c85309-6109-3fca-a143-602d80983d7d | -13.81115 | -47.93354 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0d7fe914-7487-3f6e-978a-61e9e2e276f2 | -13.83618 | -47.48992 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fdfa6adf-830a-3f47-8dae-dc549ec0a184 | -15.15573 | -46.41294 | 2025-09-29 03:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7b6f3ab-e96b-3162-8a5e-15a8274d82c1 | -12.75746 | -46.86676 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| db4ca042-f1bc-3db8-8935-e4e1561e68fb | -14.52394 | -48.4066 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f210f35f-7dbb-3103-82d8-c8940b20e341 | -13.42029 | -48.2031 | 2025-09-29 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f479b277-4044-360f-a0bb-475ea2e4d143 | -19.94317 | -43.67126 | 2025-09-29 03:49:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| d8bcc93a-f6db-3549-be6a-9a6d2cdec482 | -14.56199 | -48.26157 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce8fc6f7-222c-39f8-a3fb-7ff3c9f6f89e | -14.59471 | -45.01073 | 2025-09-29 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a39fdf06-b21d-390d-b936-556aabb1edb0 | -14.77548 | -40.08905 | 2025-09-29 03:49:00 | NPP-375D | NOVA CANAÃ | BAHIA | Brasil | 2922706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 55641123-f518-365a-9828-76ead3ec9570 | -15.26296 | -40.02148 | 2025-09-29 03:49:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d56b2138-a3a2-3bf5-b68c-da3bdac13e80 | -14.71011 | -45.20957 | 2025-09-29 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| abfef367-3910-3775-b214-faf060152ca8 | -12.7532 | -46.85874 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a268178f-05f7-3d7b-9b22-d33a68da82c8 | -14.57965 | -48.26597 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 849acbfd-6a09-3bf9-ba58-5e9685e8dc6d | -13.18682 | -47.44709 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5fa92fce-0bf7-3d4a-8e2f-bf936b3330f0 | -12.89996 | -47.11536 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 49fbcc20-75bd-31e7-8f6e-9fea42aa5d1a | -13.39196 | -48.15215 | 2025-09-29 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5555ede3-7cdc-37bb-8b6a-55727953b5bf | -23.5455 | -47.54044 | 2025-09-29 03:49:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c9ca6fdc-c347-3026-aa64-96a34ddb91b3 | -13.3799 | -48.14979 | 2025-09-29 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a85b9bfe-4d23-3476-96d0-78b8f386348e | -13.57488 | -47.29712 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d89a8311-0b6c-38fc-bc2d-b292c530e870 | -21.04776 | -44.73224 | 2025-09-29 03:49:00 | NPP-375D | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1b699db5-1131-3581-96cf-80e13f08bd25 | -14.57916 | -48.23889 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fb94d6d3-a8d1-3777-b958-c650f002570f | -14.57808 | -48.23288 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca7e57e0-36a1-37db-95f1-b8595562c3c5 | -13.57362 | -47.30358 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 181a6f40-2079-3d53-ad61-0b12930a7b3d | -13.799 | -47.90303 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 97ffff01-597f-3252-9e83-99ce1d48da46 | -13.65091 | -48.0691 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b671918-1a69-3ebd-95bc-7fb54a6fc2ab | -12.92176 | -47.15488 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 660e82d8-d6b8-3537-bb51-a67db65430b6 | -23.22079 | -49.41375 | 2025-09-29 03:49:00 | NPP-375D | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 5857e9ff-98f7-3627-8e54-690e97bb5aed | -15.04253 | -46.96574 | 2025-09-29 03:49:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e497abd-4197-38ce-96ce-a649d50ce164 | -14.53796 | -48.43412 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 82824bad-7f87-3518-bca5-11218ee2758c | -14.55183 | -48.42778 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70d74f41-9bf4-319c-affb-7c694980d296 | -13.58084 | -47.29691 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea7fb362-4ac9-3b69-8556-5819d5efd06f | -19.86535 | -43.79599 | 2025-09-29 03:49:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 45501295-1c59-33b9-b7d1-b53b4ae60b5d | -12.93444 | -46.76783 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91bb6a6b-fc9c-3760-b165-0ef5ca6231aa | -14.57775 | -48.27501 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af720581-6098-37be-80e1-dec14e1fee36 | -14.53636 | -48.43755 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3cf4a748-857e-3da2-ba06-4af634ceff11 | -15.04272 | -46.96334 | 2025-09-29 03:49:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2740cf95-c62b-3986-bedb-891e05909643 | -13.77645 | -47.864 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b435f2a-ec7c-32c8-b5d3-425f17f951e7 | -14.51907 | -48.39988 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| be016f29-2eee-37bd-8c38-2494fb2f149f | -13.22469 | -50.96144 | 2025-09-29 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f36f3501-c2e6-3ce8-bdd2-fc8192a56cdc | -13.63635 | -47.3223 | 2025-09-29 03:49:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b4f5a3e-c76f-3d33-a5d6-7e96ffd0b3e6 | -15.04326 | -46.96222 | 2025-09-29 03:49:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33efb996-6f2b-3666-b883-a8792d637c4a | -20.0491 | -41.3251 | 2025-09-29 03:50:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.7 |
| 6f60ee88-d407-34c9-acb6-88586273f5c8 | -11.8291 | -51.7937 | 2025-09-29 03:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| a46a4bbd-36b2-3e43-af78-4d39d46154f0 | -8.2662 | -45.5018 | 2025-09-29 03:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| aa3bfc3a-d5ab-3f17-9347-7059c319a9ae | -7.2214 | -44.783 | 2025-09-29 03:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 1c6b0237-bd78-3f2b-9e2e-65a6d0d5cb91 | -9.4007 | -54.6984 | 2025-09-29 03:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |


[Clique aqui para ver as próximas entradas](README26.md)
