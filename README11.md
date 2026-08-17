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
| 882004bf-2a0e-3340-8d21-23a8f410369c | -14.48241 | -45.67554 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b3e4d876-1655-391b-8fca-4e5ee696ffc4 | -14.49253 | -45.68782 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9723258-b7e5-3de6-bd10-0553c30bb4c1 | -11.99378 | -46.47248 | 2026-08-17 03:38:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c5bdb76-1518-3af2-ace0-ecba455b1010 | -14.48747 | -45.68167 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5016643f-8d79-3ed6-87c8-59a5de9fb132 | -14.8656 | -46.65103 | 2026-08-17 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e10babd-11ac-3dae-ae47-26dcbd8b9f49 | -14.89044 | -46.6286 | 2026-08-17 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddf37d55-65bc-3820-9e8e-a7bb6ad7d61c | -13.5129 | -46.28608 | 2026-08-17 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1623a77e-c322-3ec2-8959-45ea725bb5fa | -14.30113 | -47.1986 | 2026-08-17 03:38:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 84c78ecd-6baf-3a63-8aa8-8cf0111e2e92 | -13.52972 | -46.27377 | 2026-08-17 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2afc76fc-c182-3c12-bb44-b24c6ead83e8 | -14.88113 | -46.64085 | 2026-08-17 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9a707165-1c24-3678-b0db-37395268a3a0 | -12.0442 | -46.44894 | 2026-08-17 03:38:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f4363a8-f525-3018-9d3f-26bf0f429ec5 | -13.44459 | -43.84665 | 2026-08-17 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bbe2f38b-5d74-3bae-be39-b7025a78c6d6 | -12.25719 | -45.88223 | 2026-08-17 03:38:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b4fb7e9-21ae-3ee6-b1f5-2b7e562e30ee | -14.48939 | -45.67414 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5dd3473e-f9ff-3eeb-a5df-19fe7883db97 | -13.51505 | -46.2433 | 2026-08-17 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0396d63d-dbb4-3722-b2aa-cadc39aa7750 | -11.97898 | -46.44403 | 2026-08-17 03:38:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33ff7c18-5a04-3970-8ca5-77863e75e45f | -11.90789 | -47.35796 | 2026-08-17 03:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4d5355d3-0364-39fb-93a7-af15c8bff27b | -13.44541 | -43.84264 | 2026-08-17 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5df406c2-b47f-394e-9da8-b03fe81fb958 | -14.47427 | -45.68557 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 13e9fc07-f0a0-3c3d-8383-e4d3dc81d0b7 | -14.49953 | -45.68458 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf52c3ff-bb86-3511-bcc6-3805a5bf8d24 | -14.8821 | -46.63637 | 2026-08-17 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 02246108-3861-346c-8d83-f28b2ee7acfd | -12.01557 | -46.50092 | 2026-08-17 03:38:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73ac67f2-063a-3417-9cdb-c9bbd00b719b | -14.88008 | -46.6457 | 2026-08-17 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0fef78ca-81ea-37df-b27f-561df9e0cf9a | -14.49448 | -45.67836 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ee6543e0-ee19-3121-be03-9b95c0de9ce3 | -15.08887 | -48.72625 | 2026-08-17 03:38:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40961f04-a56b-3de1-9318-ea9f863e0bf1 | -15.08864 | -47.0207 | 2026-08-17 03:38:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b90ee065-f7e7-37bc-a150-5a90dce7d056 | -14.97406 | -46.58716 | 2026-08-17 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef63a2a5-56a4-393c-b756-0deaa6e55ad3 | -14.48143 | -45.68027 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6c31864d-b0b6-307d-811b-266383e0b580 | -13.50549 | -46.23105 | 2026-08-17 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 80bb689e-e4d3-3b36-8283-d20e36023936 | -13.52283 | -46.2378 | 2026-08-17 03:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bbf6942-f44c-350c-8af0-261cf93d6d9d | -13.51466 | -46.28183 | 2026-08-17 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5a912de9-c600-3ed9-9e44-d72dd271a6aa | -13.51223 | -46.25702 | 2026-08-17 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f943dd61-d3ff-36b2-b6ec-49df80ca8955 | -14.47732 | -45.67137 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5fc4fde8-1d99-3277-8016-6957e8f107ac | -14.30901 | -47.19433 | 2026-08-17 03:38:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae3e2997-f466-3ec9-9aa9-9ca31786d94d | -13.50305 | -46.23698 | 2026-08-17 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b43726f4-62ad-32cc-a36a-86909adf1ec7 | -12.00835 | -46.46892 | 2026-08-17 03:38:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2e709c41-6b2c-318e-a431-9d9481e8907b | -13.4406 | -43.84163 | 2026-08-17 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 905a2efa-6120-3ac7-b283-039b52b81655 | -15.08731 | -47.02672 | 2026-08-17 03:38:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8cd97602-74af-3a17-b504-5b3c91ce42cc | -12.26327 | -45.91769 | 2026-08-17 03:38:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f7bc03c-bb2b-32a5-8c2b-1110cad10e1c | -13.52854 | -46.27933 | 2026-08-17 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 612b1d86-696b-3bce-bdf5-e643ed7176d7 | -12.00045 | -46.47369 | 2026-08-17 03:38:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f84785b2-273e-3cfb-8492-819d64375eec | -13.51299 | -46.25834 | 2026-08-17 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 73ea4bd9-5a51-3bc8-badf-a6d289e2c4fa | -15.1697 | -48.64642 | 2026-08-17 03:38:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4234cf38-aec6-3e3d-a03c-65b586843d37 | -14.29985 | -47.20441 | 2026-08-17 03:38:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3767d6f-b44b-3413-9a6d-59a540e468da | -11.97655 | -46.45559 | 2026-08-17 03:38:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0fecc15-2b1f-33b1-a601-385515bc127e | -18.80684 | -46.73394 | 2026-08-17 03:38:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f0b17f48-77a5-3c47-813a-ba2d71dbd751 | -11.97435 | -46.44853 | 2026-08-17 03:38:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c21969e4-38a5-304e-88de-dacb997538b2 | -13.51592 | -46.24461 | 2026-08-17 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 386425cf-98fa-3dfc-b423-acc97720c95c | -13.51175 | -46.29163 | 2026-08-17 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5042b0e0-bb13-317c-82f8-9270cf06e48f | -13.43903 | -43.84571 | 2026-08-17 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6aa4d41c-b9fd-3bcb-b734-f7c2fbf72ef7 | -13.52374 | -46.23917 | 2026-08-17 03:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1a998d8-54bd-3a2f-918a-0dde32eb0b9c | -13.51115 | -46.29826 | 2026-08-17 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eac302e4-54a9-3fe5-8bb2-f671c502df1e | -12.04905 | -46.45869 | 2026-08-17 03:38:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04e35c57-cb9b-3384-ae29-b212252dee7a | -13.52168 | -46.24337 | 2026-08-17 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d58c99a8-53f4-32cd-b474-519dafcfd183 | -18.80581 | -46.73847 | 2026-08-17 03:38:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1598d76e-0571-3f20-bb87-a55c93930b52 | -13.43982 | -43.84189 | 2026-08-17 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7106c99b-af5b-32e1-921b-7aeaced81b92 | -14.4744 | -45.68364 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0043b1bc-b6ea-3cd2-9e86-93d8f7957ae8 | -13.50689 | -46.22455 | 2026-08-17 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e2b8f80d-3bbf-301e-8071-6d315e09e1e3 | -14.48844 | -45.67696 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 415a8239-df13-3149-b185-4c032bd8d412 | -14.48045 | -45.68501 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f6139404-d29e-39ff-8806-2f19890d29b9 | -15.60548 | -47.87088 | 2026-08-17 03:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dbe1d8c7-dc51-37ab-a09d-47f546bc5fd4 | -15.60403 | -47.8772 | 2026-08-17 03:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a97cba1-f18a-332c-88ea-32980a09d8d0 | -13.50659 | -46.25708 | 2026-08-17 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 711284c0-fe29-3675-b0a5-de62e06f2ce7 | -12.04668 | -46.45049 | 2026-08-17 03:38:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a39ea43-713c-3658-a25e-168f8deb2907 | -14.48335 | -45.67276 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 22cb8291-365a-3e89-837f-9372d2a83c66 | -14.46924 | -45.67948 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f3b8ddb-047f-3fbb-a55f-9d54ad09ed3f | -14.47538 | -45.67888 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fddb29d9-7623-3c22-90b6-6c894bf2b1f7 | -14.48839 | -45.67884 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2b3dbb6-5b74-3849-9707-66c18e7c8b84 | -12.01435 | -46.50682 | 2026-08-17 03:38:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6179623f-8e2c-3de6-8f19-89f6b0137fe1 | -12.17733 | -45.15022 | 2026-08-17 03:38:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e71d2aeb-a6d3-306a-bf09-e06a85d89b2c | -14.89699 | -46.62906 | 2026-08-17 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41dc8c3a-10f9-3ec8-b669-9d16569f3d06 | -13.5309 | -46.2682 | 2026-08-17 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c3314e6-8ab4-380a-a5ee-40508617b717 | -14.47637 | -45.67415 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7913f855-74ca-3738-a3e2-50e34b57477d | -13.51348 | -46.28735 | 2026-08-17 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76d945e9-b983-37e5-b2f9-65faa813bc75 | -14.8717 | -46.65367 | 2026-08-17 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 98da02d6-5096-3d99-8ec9-df55a743327f | -15.16799 | -48.65394 | 2026-08-17 03:38:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 89cc1422-1714-3c46-8cfb-7ae704317557 | -14.97293 | -46.5924 | 2026-08-17 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1125bead-8501-3600-af4b-723ab7618496 | -14.3024 | -47.19276 | 2026-08-17 03:38:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d52dd894-2a4f-335a-97fe-372b6960d50b | -6.6199 | -58.9643 | 2026-08-17 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 40fa60f3-e627-3754-8319-dcc17074ed12 | -10.5085 | -50.0228 | 2026-08-17 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 310fe895-c2e0-3379-9b75-986da5587f0e | -6.6015 | -58.9651 | 2026-08-17 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 8c61aa38-7ce6-3b7a-84ff-317a4656f371 | -16.236 | -57.6465 | 2026-08-17 03:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.2 |
| 6b043c3f-7f35-3ecb-ba29-edfeed83818b | -6.6384 | -58.9636 | 2026-08-17 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 7d64c7bc-bda4-384a-8b2f-1aff19771115 | -6.6385 | -58.9442 | 2026-08-17 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 976ff3ef-c5a8-30db-93d7-8df715892b54 | -15.9189 | -55.531 | 2026-08-17 03:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 63836d43-512a-3bdc-97e0-3cee73132918 | -15.8994 | -55.5334 | 2026-08-17 03:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 112.9 |
| e97786b7-b2f8-3cce-91ac-ec42b9312efe | -6.7123 | -58.9412 | 2026-08-17 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| bd89c8c5-7aa2-3f35-baa8-f4b553032dd2 | -6.6568 | -58.9628 | 2026-08-17 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 086ba6b6-e355-3cdb-9a62-93c5ac6439ba | -20.12227 | -44.86231 | 2026-08-17 03:40:00 | NOAA-20 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| afa7117f-75f3-386b-9323-cf50605b20c6 | -22.38265 | -47.25573 | 2026-08-17 03:40:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6463135e-1580-3b53-b76b-61ebce079f4e | -6.7123 | -58.9412 | 2026-08-17 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 0cd15290-dceb-33cf-a1bf-175ff1a6932b | -6.6385 | -58.9442 | 2026-08-17 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 7b585631-b972-3a47-b7b3-41300c757c92 | -15.8994 | -55.5334 | 2026-08-17 03:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| ec180343-d906-39f1-af51-aa2a44c49fe0 | -15.9189 | -55.531 | 2026-08-17 03:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 2eda3cac-3dbd-39cd-8cf4-0c936d349e98 | -6.6015 | -58.9651 | 2026-08-17 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 8c5c0abf-b7ac-3aa5-9abf-d22a2903a336 | -6.6384 | -58.9636 | 2026-08-17 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 143.2 |
| 9e988acd-68a7-35d6-b5fb-1b2651e98318 | -6.1106 | -57.7425 | 2026-08-17 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 8490ced4-9228-330a-acaa-6dd3dfdc35f3 | -6.1107 | -57.723 | 2026-08-17 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| e2be7975-5768-396d-b7b6-eda89a60ded2 | -6.6568 | -58.9628 | 2026-08-17 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 119.5 |
| be03ac34-6404-3b04-92df-4e003d54a6cf | -6.6199 | -58.9643 | 2026-08-17 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |


[Clique aqui para ver as próximas entradas](README12.md)
