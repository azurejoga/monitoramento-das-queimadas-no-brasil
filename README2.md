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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52486077-a649-3d6e-b9bd-8888c7c15388 | -13.47173 | -42.97965 | 2026-04-08 04:29:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 28cdaa72-d0e4-3366-a43a-5a5972b7d21d | -13.03745 | -45.0607 | 2026-04-08 04:29:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9797d41b-a2a8-37e3-9967-0dd367b4db78 | -12.02456 | -45.24469 | 2026-04-08 04:29:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80f4209e-c1c1-3bda-8bd1-79ec9520e251 | -13.03212 | -45.07244 | 2026-04-08 04:29:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1f85109-5e56-33d1-9b76-e36dad0a0727 | -12.98978 | -54.67845 | 2026-04-08 04:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb13fb5f-5b36-3d7f-b091-e92d0c34e047 | -14.44087 | -45.62947 | 2026-04-08 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d68dde1d-0932-386e-b3f3-0cd122d2d359 | -13.03272 | -45.06836 | 2026-04-08 04:29:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cbecf034-53d7-3c09-bdd9-c8ef53f1d202 | -20.83595 | -47.27763 | 2026-04-08 04:32:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 942098ce-341e-39b5-80d5-66662f6c78e0 | -13.69867 | -55.69347 | 2026-04-08 04:32:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0439fa32-18f4-3da6-b377-8bffdb6fe414 | -13.69295 | -55.69776 | 2026-04-08 04:32:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| df96f30b-3003-3061-a851-388783deb1f3 | -13.69966 | -55.68821 | 2026-04-08 04:32:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c6741732-46ac-33f9-8c11-8da1a3626e43 | -13.69493 | -55.68723 | 2026-04-08 04:32:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 66e64308-6240-3e7a-aa49-5e48242be674 | -13.69394 | -55.69249 | 2026-04-08 04:32:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 26849018-49fb-3705-9f8e-aff7f639aacb | -21.67814 | -46.74713 | 2026-04-08 04:32:00 | NOAA-20 | DIVINOLÂNDIA | SÃO PAULO | Brasil | 3513900 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 77736952-db8d-3e4b-b2e5-85744297343d | -18.21634 | -45.04916 | 2026-04-08 04:32:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 531d92b9-b59e-3010-acb8-4c51214e5a91 | 2.37332 | -60.9572 | 2026-04-08 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b369722d-1f06-3b4b-a43f-42ff78d34494 | 3.2352 | -61.20001 | 2026-04-08 05:16:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8433fb93-e5da-3a5f-9746-cdcf0d39d082 | 3.23056 | -61.19565 | 2026-04-08 05:16:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d7882b4-c35b-3d85-be26-c5e4fc99a773 | -1.82558 | -54.50873 | 2026-04-08 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15af9368-ff33-32a4-9980-559670f5aa05 | 2.36953 | -60.95776 | 2026-04-08 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50ca0d0d-e616-32dc-945a-f33c586f10eb | -13.69885 | -55.69606 | 2026-04-08 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2960d89-69ea-3e53-b0a9-6352f0a1adf7 | -15.70827 | -56.1228 | 2026-04-08 05:21:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8fab779-11ff-3147-aae8-ea8fa5bc7183 | -14.2006 | -57.4238 | 2026-04-08 05:21:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3fc8999-4271-3659-95a3-22e85e16b816 | -13.30831 | -56.69056 | 2026-04-08 05:21:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| de3a6c98-1cb3-33ee-b935-33f1ed912903 | -12.99498 | -54.68141 | 2026-04-08 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f526856-af1d-39e8-b35e-aa08ba6871e8 | -11.60565 | -55.3254 | 2026-04-08 05:21:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82d18492-7126-3d1e-965d-4ddead8de1dc | -11.93704 | -54.45807 | 2026-04-08 05:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 061e42fb-0d50-3a0e-b143-8e73c05cc9ab | -13.69954 | -55.69086 | 2026-04-08 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6aa0b081-37b5-3240-a111-485f76f660c0 | -13.69679 | -55.68935 | 2026-04-08 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b9d570b2-05a2-3702-b14a-96ba6680bcf0 | -11.93442 | -58.07618 | 2026-04-08 05:21:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4ee849d-8d95-3c3c-878a-e9edd039898d | -13.69607 | -55.69453 | 2026-04-08 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b2440ea6-036a-32d3-8aea-bdc2db2b2b9f | -11.93385 | -58.07999 | 2026-04-08 05:21:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee168ec5-fa88-3e86-a6ac-3d72069a944a | -13.69752 | -55.68416 | 2026-04-08 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7f1e2ab-82c5-30bc-9e4a-61ba5a490373 | -12.31129 | -54.86957 | 2026-04-08 05:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c696d891-2cff-3577-8956-cd5c18cc67eb | -11.20414 | -56.87898 | 2026-04-08 05:21:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8cf8e607-6b69-3479-afc8-283a96905a95 | -13.70003 | -55.69512 | 2026-04-08 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a8c45ec0-a0bf-356b-a845-3f302abc27fc | -13.70148 | -55.68473 | 2026-04-08 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36862c7a-ba46-361b-baea-bcfa7e0d0158 | -10.72342 | -56.05001 | 2026-04-08 05:21:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04571d1e-1c45-3e49-9d32-78aff69a87a9 | -11.93844 | -54.4566 | 2026-04-08 05:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12ae5f81-b8fb-302b-9b7d-198a00e5f4ff | -11.2916 | -54.76434 | 2026-04-08 05:21:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8c658b6e-c0af-3b6d-ba6b-eea189292750 | -11.57177 | -54.57292 | 2026-04-08 05:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e977d55-b126-3d49-a20c-74d4dfffe0cf | -13.70076 | -55.68993 | 2026-04-08 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 85029ee3-3cb8-3b91-9761-4e0f2e2f3d66 | -13.70023 | -55.68567 | 2026-04-08 05:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ecf4b736-2f63-3b3c-ae52-445a41c62a2b | -12.3148 | -54.86977 | 2026-04-08 05:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55f1c1b9-f176-3172-8f18-af652790ca73 | -13.64339 | -55.45359 | 2026-04-08 05:21:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fa9f94a-cda6-385b-ac22-283f2c0ac8bc | -18.49478 | -55.49858 | 2026-04-08 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e33f1a87-ff72-3111-8406-f6c76f16d122 | -18.49805 | -55.50761 | 2026-04-08 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9c0c0e52-3fff-3797-bfe0-bece94501c9a | -18.49856 | -55.5034 | 2026-04-08 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 466859cc-fff9-3a7d-ac57-714e272aec48 | -18.49907 | -55.49918 | 2026-04-08 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fa7273e8-c602-3a5a-a7e4-5ecb73d08c4a | -18.49376 | -55.50702 | 2026-04-08 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 54a589c3-f19e-381e-b93e-427660a65833 | 2.37322 | -60.9544 | 2026-04-08 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7d31532-02f3-3932-a4c4-06d6bc0eb366 | 2.36972 | -60.95496 | 2026-04-08 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c588b5f-ec70-361d-bedf-6caa29d3251a | 3.23615 | -61.19926 | 2026-04-08 05:46:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f60ca488-1feb-38ee-a346-640476108af3 | 2.37034 | -60.95883 | 2026-04-08 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c26e60f-05cc-3cba-a6c3-2e2fab741cf6 | 3.23331 | -61.20352 | 2026-04-08 05:46:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8ce52e1-0f53-3af4-b351-448c370ecf89 | 3.23212 | -61.19609 | 2026-04-08 05:46:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cb3c020-913b-38fe-a67b-cd943e6987ff | 2.38189 | -61.45256 | 2026-04-08 05:46:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1466162b-648f-3210-ad0a-868cae5d0f02 | 3.23272 | -61.19981 | 2026-04-08 05:46:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b759dfcc-6d4c-33c7-b67e-a1caf2e1a40a | -11.93252 | -58.07915 | 2026-04-08 05:50:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 451af083-50f5-3ae8-b111-1230292e7ac4 | -11.93291 | -58.07607 | 2026-04-08 05:50:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ffea9d3b-8379-3eb4-a324-f5c567b53f4a | -10.31851 | -58.49878 | 2026-04-08 05:50:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2948e9c8-2fa7-3b16-a74d-cb88837a59b4 | -13.69662 | -55.69748 | 2026-04-08 05:53:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ccf803a5-d46a-3d49-b802-5b252a56d0f0 | -18.49656 | -55.49973 | 2026-04-08 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7d2b56cf-0141-33a7-bbeb-1be5a31e343f | -13.69764 | -55.68817 | 2026-04-08 05:53:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 91543c79-6cde-3321-9ef8-3d02e487b833 | -13.69775 | -55.68458 | 2026-04-08 05:53:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6bfc2fef-1410-375c-9244-3c45b1a5ba40 | -13.6972 | -55.68926 | 2026-04-08 05:53:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be265f12-dc5e-3aaf-b42e-bc1ef611e2ce | -13.69666 | -55.69391 | 2026-04-08 05:53:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 605492e3-64bb-39cd-bf4b-b5f8b3be1dff | -18.49603 | -55.50542 | 2026-04-08 05:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 734d6189-75c8-32e7-a42c-83fb9e9e3c08 | -13.69713 | -55.69283 | 2026-04-08 05:53:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2dfad72b-f933-3896-9c0d-e3f92e60eaa7 | 3.23547 | -61.20356 | 2026-04-08 06:08:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0054c96-12d2-3cde-9777-d6ccd7285e6a | 3.23498 | -61.20064 | 2026-04-08 06:08:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0016daba-0c50-3633-b7a7-7ebf6be01869 | 3.2345 | -61.19772 | 2026-04-08 06:08:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ab0def13-57ea-310b-a3ce-db8cca1fbfe4 | -18.49386 | -55.50235 | 2026-04-08 06:37:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 32bf1d51-a800-3306-81da-63aa9a206da0 | -13.68827 | -55.68995 | 2026-04-08 06:37:00 | AQUA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 24b2d356-b82d-373f-9906-d2a89f9dd2d8 | -13.69873 | -55.6918 | 2026-04-08 06:37:00 | AQUA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6fbc221c-a0c8-3080-b7eb-92b22dcd85f7 | -13.69491 | -55.68436 | 2026-04-08 06:37:00 | AQUA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 081d931e-9341-3286-9a9a-775d1aa73c90 | -12.0481 | -45.3258 | 2026-04-08 12:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| b1078ca8-0465-31b6-aa08-08660865857d | -12.0306 | -45.2363 | 2026-04-08 12:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 3cedb163-7c93-3b2f-9431-59e710fb4846 | -12.0114 | -45.2392 | 2026-04-08 12:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 2e606e63-2c0e-3f31-9a02-b69bf5491c32 | -3.38904 | -51.94812 | 2026-04-08 12:42:00 | TERRA_M-T | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cab5c0f3-5ba1-3d7f-b6e8-9ea6f9f56ad6 | -10.79913 | -53.55841 | 2026-04-08 12:44:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 7ad26027-e9da-3c0f-a24b-e933cfaa0659 | -13.15203 | -53.10805 | 2026-04-08 12:44:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 9fbe13c4-daae-3ad7-ba6b-98610db57fab | -12.04344 | -52.87514 | 2026-04-08 12:44:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 07a7b016-d446-34d0-a4f5-50fb1f7f8b9d | -15.40556 | -56.2868 | 2026-04-08 12:44:00 | TERRA_M-T | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e4c6b5ba-53fa-3dcb-8d35-d083bb0ac5ad | -13.69679 | -55.68754 | 2026-04-08 12:44:00 | TERRA_M-T | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 3714e260-abad-3719-abdd-5a66dc5b5130 | -13.69969 | -55.68145 | 2026-04-08 12:44:00 | TERRA_M-T | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 31bf9a71-aa8c-3a65-b8d8-95486c8ac4a0 | -14.87814 | -52.36709 | 2026-04-08 12:44:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| a04b30dc-0ff0-3601-8af2-7c357cd0c50e | -15.43945 | -54.24691 | 2026-04-08 12:44:00 | TERRA_M-T | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 444beb21-3b7d-393f-a6bf-75f085453c97 | -12.99589 | -54.67966 | 2026-04-08 12:44:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| d06de042-dab5-3fb5-9e27-8cf7d366765d | -11.20429 | -51.54574 | 2026-04-08 12:44:00 | TERRA_M-T | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 523fa7c3-abdb-3012-be62-53371b6823cf | -14.99907 | -56.27628 | 2026-04-08 12:44:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| db306ccd-7d34-37e2-b6d6-7b55133f0515 | -11.19775 | -51.55046 | 2026-04-08 12:44:00 | TERRA_M-T | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 4f24d7d9-505d-341c-b355-055d97704f89 | -12.23704 | -57.7834 | 2026-04-08 12:44:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 87beec10-beff-30f6-bcda-27c412a7a754 | -12.33376 | -52.08538 | 2026-04-08 12:44:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 8b88fa2c-796d-3021-9372-4507d7e93251 | -13.15881 | -52.39024 | 2026-04-08 12:44:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| fcd0c0df-b372-33d5-bfd6-26b01393f0d7 | -12.99384 | -54.67354 | 2026-04-08 12:44:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a2362a45-3df6-3eaf-8d33-16c90329e61f | -13.2899 | -54.79345 | 2026-04-08 12:44:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ff042be9-8e0f-3d66-afe6-54be21da6265 | -11.22112 | -52.24501 | 2026-04-08 12:44:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 8c0af16c-813f-366a-a093-e8afd45ab5d2 | -14.24417 | -54.93273 | 2026-04-08 12:44:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 95f8d8c4-fe74-3e76-bc6c-fb6b296086bb | -13.15588 | -53.42933 | 2026-04-08 12:44:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |


[Clique aqui para ver as próximas entradas](README3.md)
