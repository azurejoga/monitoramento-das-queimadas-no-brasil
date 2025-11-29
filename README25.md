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
| 33e6a60b-cfbd-37bf-b7d4-eb289c85aaee | -20.2198 | -47.53009 | 2025-11-29 04:46:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95172872-27f3-3a73-bc80-8e5ee7a4cdda | -20.18292 | -52.37514 | 2025-11-29 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 17.4 |
| a542189d-4b9b-325a-937d-c2d5e2c90e65 | -20.75119 | -47.20504 | 2025-11-29 04:46:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a0dad30-cbf9-32f7-9685-671bc79fc97a | -18.79577 | -48.02266 | 2025-11-29 04:46:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9f11f93b-6e84-3337-ad37-882fe13c92a3 | -19.12602 | -52.70528 | 2025-11-29 04:46:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 982414f0-f86e-3f78-b1c9-db3679322ad9 | -18.11885 | -47.13286 | 2025-11-29 04:46:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a490f531-ac74-385d-86bf-56fbb3cba514 | -20.18785 | -52.38734 | 2025-11-29 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c35ea328-e7c2-3811-a630-7b80f3d54f1e | -20.18842 | -52.38367 | 2025-11-29 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8bc8387f-32ab-37c7-9cde-f4fd89db19ce | -16.19439 | -59.33257 | 2025-11-29 04:46:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67ea7826-8e14-358b-8d25-722b30f42060 | -15.93883 | -59.84634 | 2025-11-29 04:46:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa234207-e880-3010-aee2-151fb3fda409 | -17.61188 | -46.66023 | 2025-11-29 04:46:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ec9f914b-0360-349e-a72c-3c34f0f3c16c | -20.1929 | -52.37689 | 2025-11-29 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b9fb8e5c-fb91-3f47-915c-95e07798558e | -17.48567 | -57.12982 | 2025-11-29 04:46:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9dbfff71-b6a7-3005-9527-d16f0e0d0f06 | -18.13888 | -47.13591 | 2025-11-29 04:46:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d6c240bf-7392-3c0e-bad1-27cad6b3ad9e | -14.74537 | -50.06437 | 2025-11-29 04:46:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2225c0de-fa34-3267-8baa-ef56cafd9947 | -18.13017 | -47.13995 | 2025-11-29 04:46:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9080002c-f25d-38b8-ab9e-be320cd70130 | -20.18682 | -52.37205 | 2025-11-29 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d15767a-878c-319d-a489-ed0f0f426383 | -19.89363 | -57.444 | 2025-11-29 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 16c48714-dae9-312d-bfc4-0f95127ddcf0 | -19.33731 | -54.17242 | 2025-11-29 04:46:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50f0315b-ee06-39ef-b1a2-a7606c48986c | -19.79684 | -56.09515 | 2025-11-29 04:46:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fb9fa19b-875f-3f67-b4d9-880c1985a804 | -19.11879 | -52.70777 | 2025-11-29 04:46:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 690f0df3-00aa-3da5-8f80-988a59d29555 | -20.17844 | -52.38192 | 2025-11-29 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dcebcde9-2790-307a-9d28-418358b9df7d | -20.72692 | -49.27336 | 2025-11-29 04:46:00 | NPP-375D | GUAPIAÇU | SÃO PAULO | Brasil | 3517505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dd2c7ad3-6bca-3631-8f03-af4a0cef4f51 | -17.48965 | -57.13063 | 2025-11-29 04:46:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 435088fa-219e-352c-b6e2-a7259606d26c | -18.17159 | -47.24006 | 2025-11-29 04:46:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8b06aacd-6f3f-3e57-89cb-3e8ed0e4fe99 | -20.98629 | -48.63078 | 2025-11-29 04:46:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3e400507-b9a5-39d3-b875-4feafa5b3644 | -20.17786 | -52.3856 | 2025-11-29 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6dbbc7e4-f0ef-3e68-8f44-f7196eccef3c | -20.17511 | -52.38134 | 2025-11-29 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5ece4cfd-e99b-3f7c-bcb5-bcbafe61e9a5 | -20.19175 | -52.38425 | 2025-11-29 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cb07b25d-c854-3e7f-9c58-0baa04dfd9a8 | -20.4157 | -47.21737 | 2025-11-29 04:46:00 | NPP-375D | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 41af02e2-5824-3dae-88eb-63c8f9ff5f70 | -18.12615 | -47.1394 | 2025-11-29 04:46:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 724fde34-88fa-3a7a-aeab-fe1cd3e62c35 | -19.79689 | -56.09726 | 2025-11-29 04:46:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4ca8ee78-8ef2-3b1e-b8d0-4794cba81043 | -19.89753 | -57.44482 | 2025-11-29 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| ea50820c-133b-37a0-bc64-c4f9f6d65b75 | -20.45339 | -47.50905 | 2025-11-29 04:46:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d1be74c5-806c-3da3-8b80-a24ef1d66af6 | -20.20948 | -47.5464 | 2025-11-29 04:46:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc590d6f-1181-39b0-9ff3-f4f11e0cc14d | -19.12935 | -52.70587 | 2025-11-29 04:46:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7b75143-a92d-3e48-8198-1a6f36f96c2d | -20.21529 | -47.53321 | 2025-11-29 04:46:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a138711-a22f-3d6c-80e7-c47ce0de1b08 | -20.75071 | -47.20892 | 2025-11-29 04:46:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c76219f4-3ecf-358c-bf88-8dbc2298d7f7 | -20.18624 | -52.37572 | 2025-11-29 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 4eded188-9e44-3913-97fc-0bfdb9494118 | -20.21577 | -47.52952 | 2025-11-29 04:46:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5ba8ddd-5e48-3bf9-a2a2-56aea2941617 | -20.17626 | -52.37397 | 2025-11-29 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 34d98611-d8e1-3ded-bbb0-61579465596d | -20.18177 | -52.3825 | 2025-11-29 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 3cb64803-7d6a-34ac-ad5d-b5df35d7a21d | -20.19233 | -52.38057 | 2025-11-29 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 433d844f-9ca5-3de9-a178-93545ecf519d | -20.18234 | -52.37882 | 2025-11-29 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 17.4 |
| e488e003-db81-30de-b1ff-30eac0daa204 | -22.97068 | -47.03152 | 2025-11-29 04:48:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c97848a9-7efd-3961-bb2f-9a26df510dff | -27.13657 | -52.58937 | 2025-11-29 04:48:00 | NPP-375D | CHAPECÓ | SANTA CATARINA | Brasil | 4204202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 45653cd6-9694-3e6d-947f-8e2b0cc8ddcb | -20.43794 | -57.92411 | 2025-11-29 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 741626d3-9660-3ce4-afa1-e50b12133ce0 | -22.72927 | -49.3438 | 2025-11-29 04:48:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b32b7407-121f-3815-91f4-a79bf61a0efc | -21.71615 | -49.46473 | 2025-11-29 04:48:00 | NPP-375D | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7ae1781d-f203-32d8-82ad-c311fc6e114c | -20.43867 | -57.92535 | 2025-11-29 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| ef5060c8-63b1-3b52-ae61-f705f8266ecd | -22.0844 | -46.82081 | 2025-11-29 04:48:00 | NPP-375D | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f1652dd-205f-35c9-8ba8-d0baf5aeab25 | -22.97681 | -46.23597 | 2025-11-29 04:48:00 | NPP-375D | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b57cee9c-f6d2-341d-b067-0d0fa2f15d6c | -20.43396 | -57.92326 | 2025-11-29 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a2ca676e-3604-3080-bf1d-d02df9682b53 | -25.17479 | -49.39636 | 2025-11-29 04:48:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 27165526-73bf-338d-8d68-363a2153a83a | -26.41638 | -51.84164 | 2025-11-29 04:48:00 | NPP-375D | PALMAS | PARANÁ | Brasil | 4117602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4b479c7e-1295-3b5c-a0ff-651d9cd2ac1e | -21.68994 | -47.95625 | 2025-11-29 04:48:00 | NPP-375D | AMÉRICO BRASILIENSE | SÃO PAULO | Brasil | 3501707 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e85904c6-2b96-38db-9dc0-db264dcca844 | -23.48697 | -45.84494 | 2025-11-29 04:48:00 | NPP-375D | SALESÓPOLIS | SÃO PAULO | Brasil | 3545001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 822f1d0a-0543-302a-8eb0-a5b75f7ab050 | -25.90962 | -52.52848 | 2025-11-29 04:48:00 | NPP-375D | CHOPINZINHO | PARANÁ | Brasil | 4105409 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 509ad82a-d10a-31e4-9c87-fff8fc544c89 | -23.134 | -50.14294 | 2025-11-29 04:48:00 | NPP-375D | BARRA DO JACARÉ | PARANÁ | Brasil | 4102703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 162d74b8-db13-34ca-8008-36f9b7e15969 | -23.1346 | -50.13848 | 2025-11-29 04:48:00 | NPP-375D | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 235f4d9b-fab6-3e52-b3db-a85a17448e4d | -22.76353 | -44.98838 | 2025-11-29 04:48:00 | NPP-375D | CACHOEIRA PAULISTA | SÃO PAULO | Brasil | 3508603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0b3b1502-0747-3868-9dd9-499de684173f | -22.76486 | -44.98877 | 2025-11-29 04:48:00 | NPP-375D | CACHOEIRA PAULISTA | SÃO PAULO | Brasil | 3508603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ee7825e5-c173-304d-8e25-714a45071e5f | -20.43469 | -57.92451 | 2025-11-29 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| a1a00d93-de56-3b9d-8b9f-50c1736069a9 | -25.17863 | -49.39702 | 2025-11-29 04:48:00 | NPP-375D | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 728826aa-6be3-3b46-a071-53cf46b51f51 | -22.08387 | -46.8253 | 2025-11-29 04:48:00 | NPP-375D | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1116b80d-889d-3ef3-b841-b81ae3db9b0f | -22.58507 | -49.59409 | 2025-11-29 04:48:00 | NPP-375D | UBIRAJARA | SÃO PAULO | Brasil | 3555505 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b612504-9de3-30ce-9a99-747dad07861a | -22.95363 | -49.06111 | 2025-11-29 04:48:00 | NPP-375D | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63264ce8-ff0d-39f0-b4d5-14c41ea456af | -23.25655 | -48.28526 | 2025-11-29 04:48:00 | NPP-375D | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b9eea163-e8e5-3d07-849c-43590de6518f | -23.25602 | -48.28341 | 2025-11-29 04:48:00 | NPP-375D | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7ced7894-5f2d-34b4-8dc0-6c6e109afc98 | -21.68724 | -47.95693 | 2025-11-29 04:48:00 | NPP-375D | SANTA LÚCIA | SÃO PAULO | Brasil | 3546900 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 768734d0-868a-3fbd-9469-16235e7870f3 | -23.13761 | -50.14351 | 2025-11-29 04:48:00 | NPP-375D | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b8fbdb00-d83a-3e78-b003-6ca8838c351a | -21.68593 | -47.95571 | 2025-11-29 04:48:00 | NPP-375D | SANTA LÚCIA | SÃO PAULO | Brasil | 3546900 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4741673-5b48-3f6d-b844-44aa637e1e5e | -8.1633 | -43.2055 | 2025-11-29 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.0 |
| 45792503-62be-3c00-9bdd-591d17959451 | -2.6322 | -48.542 | 2025-11-29 04:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| a18852e7-f865-3a10-b3c6-11d45082dc6d | -20.2016 | -52.3717 | 2025-11-29 04:50:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 7bcce876-9fd7-3b40-880a-d4facf191b76 | -20.1807 | -52.3975 | 2025-11-29 04:50:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 81.4 |
| e339814f-ccb3-3266-a3af-58610b45ee18 | -20.1813 | -52.3754 | 2025-11-29 04:50:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 195.2 |
| 90e5ac1d-0fa8-37dd-8f5b-144e3e7b4134 | -28.00304 | -54.65584 | 2025-11-29 04:50:00 | NPP-375D | CÂNDIDO GODÓI | RIO GRANDE DO SUL | Brasil | 4304309 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 166f4a26-c4ea-3fab-9814-2c64fcfcf911 | -28.63816 | -56.04481 | 2025-11-29 04:50:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| dab72ab8-bcdc-3b1e-9f2e-9b4744fca127 | -20.2016 | -52.3717 | 2025-11-29 05:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 105.7 |
| ccf8ba87-b51f-3d4f-831c-8f85be012f5a | -8.1633 | -43.2055 | 2025-11-29 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 2c650a72-3cec-35da-8b4b-0b03febea8df | -20.1813 | -52.3754 | 2025-11-29 05:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 190.0 |
| 4db5ebfa-a553-3edf-98b0-1736cd909f84 | -2.7845 | -47.4343 | 2025-11-29 05:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 340b83c9-aa99-3947-ba59-e7b12aec4a6e | -20.1807 | -52.3975 | 2025-11-29 05:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 01f82771-f21a-34c8-afb5-0f3a572cbb4e | -0.76864 | -52.33393 | 2025-11-29 05:01:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b56c1bc-249c-38dd-9a4e-dd997fed3a6c | 0.4626 | -60.43573 | 2025-11-29 05:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e168178b-4684-378b-9d55-494f3410101f | 1.07799 | -52.72227 | 2025-11-29 05:01:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7755b0bf-7e71-3599-bd48-e3d9c065507f | -1.09183 | -53.17765 | 2025-11-29 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f05fbe3e-ff98-334e-8804-6268e0a3b51d | -2.54723 | -44.60675 | 2025-11-29 05:01:00 | NOAA-20 | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5ea2401-e4bd-38ac-b5d4-49eae500606c | 0.49365 | -51.16286 | 2025-11-29 05:01:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35a34da0-e280-3a40-8e17-da3f634df90a | 1.04847 | -52.35986 | 2025-11-29 05:01:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d38447ea-3089-3b26-856b-a395392148c2 | -0.8703 | -48.65586 | 2025-11-29 05:01:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d83b4b0d-f8a0-3c75-a409-22aa8e3226d8 | -0.90909 | -52.4398 | 2025-11-29 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 904dd7d3-51bf-36a9-858a-5b88c9382246 | 0.79067 | -51.96779 | 2025-11-29 05:01:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16c44f1a-58cd-35ab-bdd3-7a92f5975d7a | -2.24761 | -46.52725 | 2025-11-29 05:01:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fef68811-806d-3274-883d-0e8bf9cf5644 | -1.48339 | -45.79287 | 2025-11-29 05:01:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e3504fd4-c1b8-392a-8877-429e3fd9b92f | -1.09571 | -54.10539 | 2025-11-29 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4a6cc6ed-0e9b-33e8-9ae9-c11fc63e56e2 | -0.75252 | -47.76038 | 2025-11-29 05:01:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ac5128b-8b65-362f-a21d-3bdd28a42713 | -0.78295 | -52.39407 | 2025-11-29 05:01:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46837f75-0a76-3c3b-9bbb-1e2d80b748b6 | -1.0879 | -53.18072 | 2025-11-29 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README26.md)
