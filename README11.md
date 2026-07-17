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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0dbcfba0-ec2e-3145-ab74-8764ebfda6d6 | -22.37985 | -49.78667 | 2026-07-17 04:42:00 | NPP-375D | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| def2af16-b1e3-39f9-ab1f-8afc6cbff6fe | -21.34998 | -51.04383 | 2026-07-17 04:42:00 | NPP-375D | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c0a28d65-4b23-3efa-ae32-6a1e082fa97d | -21.66582 | -56.33122 | 2026-07-17 04:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 600c5910-8019-3d91-a551-b0cebae1f963 | -22.46566 | -43.09623 | 2026-07-17 04:42:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| ce0f1bc5-d78d-351c-b0d5-019bd3b6e37a | -22.49178 | -44.04679 | 2026-07-17 04:42:00 | NPP-375D | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ed8e0a94-ec9a-35b4-8d37-63d674290a5c | -19.82915 | -57.94151 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ef344525-0743-3c2d-b160-aded53dc5cfc | -21.76195 | -56.30746 | 2026-07-17 04:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbabd9bc-f9c4-3057-a0bd-cf1f92c0bbcd | -22.24699 | -52.8687 | 2026-07-17 04:42:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ba43c1af-05b0-3636-b2fa-cc962c2220fb | -19.8183 | -57.94492 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e811a48e-c6c3-34dd-908e-e3e7e3e146d6 | -21.68557 | -47.93887 | 2026-07-17 04:42:00 | NPP-375D | SANTA LÚCIA | SÃO PAULO | Brasil | 3546900 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40662ae9-113a-3a55-8e65-7cb8f8b6b645 | -19.834 | -57.94265 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 98d3bf7e-cb44-32dc-855d-eefd051519d7 | -22.22237 | -55.97358 | 2026-07-17 04:42:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3177bf22-8e20-35d9-b80f-996f6cae33a4 | -19.86143 | -57.99228 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| c46499d4-6570-3611-87fd-6224b4335574 | -22.24236 | -56.05759 | 2026-07-17 04:42:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0692b035-26e1-3cb0-ba69-f6a4ed48e2ab | -22.24974 | -52.87179 | 2026-07-17 04:42:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 9f3e8ac7-bb91-3336-a3bb-5d0abd7ea27e | -22.46647 | -43.09441 | 2026-07-17 04:42:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 19.0 |
| 701311d0-ca23-3691-9e15-27a1334deafa | -23.39398 | -47.01188 | 2026-07-17 04:42:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0072aa08-83ec-316c-b030-454ff527c6d2 | -19.82431 | -57.94038 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| f34b88f9-db53-3993-aac2-7a737cbf78ad | -19.81963 | -57.96312 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 166ce6f0-b02c-3667-93ce-fd7f4ae8a3da | -19.85172 | -57.99001 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 65ba320d-9740-33ed-876b-006ba926cd55 | -22.2398 | -56.04869 | 2026-07-17 04:42:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb6d3cd4-e34c-3921-a42d-19e52f4ac0dc | -21.76363 | -56.29893 | 2026-07-17 04:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 166c431a-e710-3af8-b9b2-9c4d896f32ec | -19.8598 | -57.99055 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 53d1378f-0d4a-3e42-8ef8-935e5e46e244 | -19.85495 | -57.98941 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 45ebce39-592f-3c3d-a742-e884c4ccd71e | -23.13924 | -48.66422 | 2026-07-17 04:42:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 382455de-7b9c-34f9-a735-98a299e5e25e | -22.24277 | -52.87212 | 2026-07-17 04:42:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d8134c35-7ea3-3864-a103-3b32b2da0969 | -21.77205 | -56.30092 | 2026-07-17 04:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b4f0d5a0-4e52-3ce4-9f43-7316112c466a | -23.78596 | -48.45443 | 2026-07-17 04:42:00 | NPP-375D | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9c64b657-f50a-34ea-95be-5cce73d8509f | -22.25023 | -56.0174 | 2026-07-17 04:42:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 407f61dd-a63d-3813-835f-755b2cb75a85 | -19.84524 | -57.98712 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| cb39f630-967b-35ca-8d44-95118c6bc71a | -22.23999 | -52.86725 | 2026-07-17 04:42:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5dd6a41c-dc75-3b27-b780-5512ae3ecec2 | -19.81478 | -57.96199 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b384bf0a-9628-3aa0-b39c-b8c95128efed | -22.46693 | -43.09021 | 2026-07-17 04:42:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 20.5 |
| 4e7b34d9-fc87-3af7-861c-ac4c0e594d46 | -19.8464 | -57.9814 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b10e2b04-d816-37b0-b2a2-4699388597a6 | -21.77122 | -56.30512 | 2026-07-17 04:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8b2d11da-478b-302e-898c-23a0d6ffb6b0 | -22.24349 | -52.86797 | 2026-07-17 04:42:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| dd16703a-cd1f-380d-835c-d6bd5621e517 | -19.85658 | -57.99114 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 8628d24c-3605-3645-bb2b-741ce323ee17 | -22.24624 | -52.87107 | 2026-07-17 04:42:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| eeeaa9d4-004e-3383-8a28-ddf69e85e8fb | -22.4709 | -43.09619 | 2026-07-17 04:42:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 59d5dc4c-96ab-364d-a128-69e5e43a273d | -23.19966 | -48.25369 | 2026-07-17 04:42:00 | NPP-375D | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 7056cf92-7d04-3602-852b-6e1123448db2 | -21.34663 | -51.04321 | 2026-07-17 04:42:00 | NPP-375D | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c7f9b8f1-f238-37de-80c9-7dcba7c18e25 | -22.22061 | -56.1025 | 2026-07-17 04:42:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d6ac79d0-7847-339c-bf47-60c4f43d7d26 | -22.65364 | -43.64996 | 2026-07-17 04:42:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| edf48ab4-dd58-3d41-855e-b78408dd23c9 | -21.77039 | -56.30937 | 2026-07-17 04:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ec39044-a0db-3c3b-9b74-bf78f53ee543 | -22.65803 | -43.65067 | 2026-07-17 04:42:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9b974378-9b23-30cf-909f-ba67ee0a21b4 | -23.14207 | -48.66875 | 2026-07-17 04:42:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4047afc6-9c7f-3ac3-901d-48b9b3016aa2 | -21.66162 | -56.33012 | 2026-07-17 04:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3eb5f9d9-f2ae-362c-a5fd-67b48abb47fc | -22.30687 | -48.01933 | 2026-07-17 04:42:00 | NPP-375D | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fafb311d-1ffa-3835-87d1-cb125c994afd | -19.82699 | -57.97681 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| d0aa4138-a440-3ac8-87d1-34b563e3604f | -19.84155 | -57.98026 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 35cc92ef-6a30-33c0-897d-074a714b73e1 | -22.24627 | -52.87285 | 2026-07-17 04:42:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| d63d7567-cb78-3b9a-8b7d-0c193b8bdd02 | -23.13865 | -48.66821 | 2026-07-17 04:42:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99e9cb59-9c01-39d3-be05-c06210aeef50 | -21.76701 | -56.30413 | 2026-07-17 04:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| db8859ed-36fb-3c72-b3a3-7c66432ca44f | -22.47007 | -43.09797 | 2026-07-17 04:42:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| a7e65335-6c07-3fb6-956d-4ab3a1c01ace | -23.13806 | -48.67218 | 2026-07-17 04:42:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cedfa978-950e-3660-9a6f-31ec091d23e8 | -21.66246 | -56.32587 | 2026-07-17 04:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a0d6fdf-46ba-3c1e-a70b-7af2a289d167 | -19.86466 | -57.9917 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 941d1cf2-730c-354f-9ec9-01757e334ea0 | -19.8367 | -57.97911 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 51c8b52e-8e91-3bff-b380-88b10117f069 | -22.66242 | -43.65136 | 2026-07-17 04:42:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3d8ba9b6-5154-3b2e-aca7-542e4179f80c | -19.82214 | -57.97567 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 108b9254-36dc-3cb3-9421-87a419210314 | -22.63833 | -43.66654 | 2026-07-17 04:42:00 | NPP-375D | JAPERI | RIO DE JANEIRO | Brasil | 3302270 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d1cd901d-18bf-3020-9126-239f0997ee05 | -23.62783 | -46.07301 | 2026-07-17 04:42:00 | NPP-375D | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 13e9ff4d-8b77-3c8b-b04b-c6303b4f47c4 | -22.92246 | -49.20325 | 2026-07-17 04:42:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 19c36a6f-124c-3004-bcd1-014933222b08 | -22.23927 | -52.8714 | 2026-07-17 04:42:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 38a9c01b-48a8-31e7-a731-1e05f2417ba0 | -23.10191 | -48.75096 | 2026-07-17 04:42:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43033c51-3dfd-3e15-9157-4c726ebd7a21 | -19.83184 | -57.97796 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| d5508303-9cfd-3c6b-a095-a8d1d16df65e | -23.14144 | -48.66792 | 2026-07-17 04:42:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68dda10e-a386-39de-9a34-97bc1fe310c8 | -22.24977 | -52.87358 | 2026-07-17 04:42:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 2b8e5dbc-3195-3adb-afcf-14ee4c52d7d9 | -22.97844 | -48.9233 | 2026-07-17 04:42:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4698184-035e-3f45-bf27-037022968d1e | -19.83884 | -57.94379 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d1234009-e3bb-3197-8df7-14097a35c833 | -21.67254 | -56.31949 | 2026-07-17 04:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0b911fe9-da82-33d6-a3ce-5928aa0b8dfb | -19.84807 | -57.98317 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 57862bce-552f-3a13-bd0f-2f791214b700 | -22.80719 | -43.55217 | 2026-07-17 04:42:00 | NPP-375D | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 737ae80b-e815-30d8-8618-465b3f491a95 | -22.23904 | -56.0526 | 2026-07-17 04:42:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1eb2c9fe-74e3-3c1c-a74a-887b1e217741 | -22.46614 | -43.09209 | 2026-07-17 04:42:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 25.2 |
| ad1814ee-af42-3296-a1c5-155e9e35af39 | -22.91573 | -49.20206 | 2026-07-17 04:42:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d1cf94f0-d66d-3de6-aeb5-e1452cfdbc95 | -22.97902 | -48.91942 | 2026-07-17 04:42:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0fb3158e-9993-313b-b5e8-406200276113 | -19.85009 | -57.98826 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b21c4cc2-6038-37d0-8386-94f72275a00b | -22.46599 | -43.09872 | 2026-07-17 04:42:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 19.0 |
| 56354f2e-25d9-3f5b-be09-3b82b832a509 | -21.76617 | -56.30841 | 2026-07-17 04:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 094ad836-d332-3a34-a93b-dffb6a601937 | -19.81595 | -57.95629 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 8dcd6ba2-739b-3427-b5dc-a690c57f8404 | -22.24205 | -52.8763 | 2026-07-17 04:42:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| bb67df3b-9706-3cdf-836f-0412b5a074f5 | -23.50407 | -48.57038 | 2026-07-17 04:42:00 | NPP-375D | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d088273b-1a85-34eb-a6ea-9318ffc8bb5f | -22.47138 | -43.09181 | 2026-07-17 04:42:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bd0cc8da-00b1-38e9-af24-e91704ab69e9 | -19.84322 | -57.98204 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 43a477f7-9a19-301d-a291-8189506c5744 | -22.47056 | -43.09374 | 2026-07-17 04:42:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 25.2 |
| 2877907b-7cdc-3765-a5f9-062386287e9f | -19.82331 | -57.96997 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 3feb7923-0b75-398c-932c-1c7593721679 | -22.46514 | -43.10065 | 2026-07-17 04:42:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| c56cfffb-c24b-378f-a251-1c8387ca8543 | -21.66329 | -56.32163 | 2026-07-17 04:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 155310a7-6e6e-3dc4-81f1-94cc679a69d0 | -23.78537 | -48.45847 | 2026-07-17 04:42:00 | NPP-375D | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 84f72b3b-cbb1-3c2c-b536-b88ec55005d6 | -22.22058 | -55.97214 | 2026-07-17 04:42:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68966393-4a7c-3166-adf0-1e5c550f86ba | -22.23571 | -56.04763 | 2026-07-17 04:42:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83433fea-bac7-38ac-89c7-e67319076d1f | -23.13582 | -48.66366 | 2026-07-17 04:42:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.2 |
| c4b5f773-b343-3617-84a4-591f34edbc0d | -21.66749 | -56.32271 | 2026-07-17 04:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e80cc5b-5add-3a38-8879-d2c1d44c7f5d | -21.7628 | -56.30317 | 2026-07-17 04:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d8fdb32d-12ba-35c5-a4bd-d06315a1c324 | -21.76784 | -56.29992 | 2026-07-17 04:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f6ce1eb1-e266-3969-b352-6a99202375e6 | -22.24551 | -52.87523 | 2026-07-17 04:42:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| ab4b06eb-5dfd-3706-8136-7374ef5f6e8b | -19.85292 | -57.9843 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 81f2b084-20f8-3125-bdbe-4ddce0c66fec | -19.82314 | -57.94606 | 2026-07-17 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| fc31bb28-2af0-32da-895a-519f22f27be6 | -30.69538 | -52.56223 | 2026-07-17 04:44:00 | NPP-375D | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |


[Clique aqui para ver as próximas entradas](README12.md)
