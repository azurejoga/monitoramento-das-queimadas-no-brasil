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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f934846-a121-359b-b846-64c1ee4659e6 | -20.4391 | -47.70774 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 649ee4cd-5927-3884-aa0a-4214e2a79b98 | -20.43829 | -47.68861 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 148df6ed-eac6-3975-bade-e2c508d28698 | -20.43817 | -47.71198 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 15.6 |
| b1e0259d-be95-3a1b-ac86-4df668cb1c23 | -20.43731 | -47.69295 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 142d19e4-88a3-3f7c-9915-99eba8d44c4e | -20.43635 | -47.69714 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 1f165e4e-5c15-3ccf-b3c4-45b365b5564f | -15.16741 | -47.07654 | 2024-10-07 03:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31024998-af49-395f-9c04-141f3227c607 | -15.16627 | -47.08181 | 2024-10-07 03:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d89d6ee3-3d97-34ae-a571-045ed8b309e8 | -18.09454 | -47.83873 | 2024-10-07 03:38:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e96c9cc7-20da-3ebf-ae9a-920433bd2a42 | -18.09354 | -47.84327 | 2024-10-07 03:38:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e83a9b48-18ae-3742-8434-d56cbe25fb08 | -20.20151 | -48.71585 | 2024-10-07 03:38:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ff7db37-f0a7-38da-a40d-5898e32e01e3 | -20.19605 | -48.71243 | 2024-10-07 03:38:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c6a23dd8-98fb-3b22-9da4-2e2170798ed1 | -20.19543 | -48.71444 | 2024-10-07 03:38:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b643005-58e9-3079-afe0-49728c782239 | -16.14576 | -48.89207 | 2024-10-07 03:38:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b243be7b-f658-359f-92a8-7fdbb0d47d00 | -16.14445 | -48.89782 | 2024-10-07 03:38:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2618601b-4f99-3814-80a4-2bada6ab7cdb | -16.14314 | -48.90353 | 2024-10-07 03:38:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 91be7d51-8b15-3b9d-a2f6-ea335517e19c | -16.14268 | -48.89183 | 2024-10-07 03:38:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9eefbe42-36de-37d1-bf88-4a27b5690f2d | -16.14139 | -48.89764 | 2024-10-07 03:38:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3f12718b-ef9d-385c-ba5b-49690804fcaf | -16.14012 | -48.90335 | 2024-10-07 03:38:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a399863c-2e13-3dfe-8d4a-b455eacf277e | -16.1347 | -48.89649 | 2024-10-07 03:38:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8fde275e-dd23-3186-b590-cb330231d0e1 | -16.13338 | -48.9024 | 2024-10-07 03:38:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0374d31a-9709-3bd8-b3f8-917fca6a23d7 | -16.09571 | -50.22668 | 2024-10-07 03:38:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5d975d01-6c32-3eb4-8716-f5d7ec83a5dd | -16.09506 | -50.2207 | 2024-10-07 03:38:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 45330a5b-7cab-303e-bb60-81081259d95c | -16.09093 | -50.21507 | 2024-10-07 03:38:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ba7e2d3-dd13-3c66-91a4-048101e8b009 | -16.08916 | -50.22263 | 2024-10-07 03:38:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 927bb7f3-d3d2-3a4a-aa7c-723646ce05c8 | -16.0886 | -50.21619 | 2024-10-07 03:38:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0e756b0-101c-3244-953f-6cfc76df2cfa | -16.08268 | -50.21826 | 2024-10-07 03:38:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3f88c62-70c9-316f-bcb3-6ead0a599762 | -16.08207 | -50.21197 | 2024-10-07 03:38:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c89dbd7e-43a2-3aef-b320-62c4861e5a2b | -16.08026 | -50.21989 | 2024-10-07 03:38:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 32169293-f0e2-300a-9edc-8291afdaac3b | -16.0752 | -50.21823 | 2024-10-07 03:38:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 075f01d5-4107-36a4-b6f1-7274e51a2d23 | -16.07222 | -50.22238 | 2024-10-07 03:38:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 40ac8118-2972-31f8-8926-9fd6911e1cb8 | -17.26274 | -49.22337 | 2024-10-07 03:38:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4961eed6-321a-3754-8a90-4b45323a81b4 | -19.16422 | -50.64058 | 2024-10-07 03:38:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 95432839-5190-3363-8680-f5e3b6fde214 | -19.16254 | -50.64758 | 2024-10-07 03:38:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ee97f6f0-eefc-36b5-888d-6cc37c6fb192 | -19.15898 | -50.63211 | 2024-10-07 03:38:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f3a414fe-62b9-34de-afda-b0f63122a5c0 | -21.84344 | -46.93464 | 2024-10-07 03:40:00 | NPP-375D | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 028d27ca-aa14-382c-b9ba-b61c4b846d30 | -21.84266 | -46.93818 | 2024-10-07 03:40:00 | NPP-375D | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 49365f93-8a31-32a6-a822-5a010486b99b | -21.71134 | -42.29379 | 2024-10-07 03:40:00 | NPP-375D | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 95e7c62f-e975-32df-8e90-87e16e6434e2 | -21.7074 | -42.29268 | 2024-10-07 03:40:00 | NPP-375D | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 97ff27fb-2cbf-3b77-8fef-ad1ab00a1012 | -21.70637 | -42.29811 | 2024-10-07 03:40:00 | NPP-375D | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 16017be3-3b28-3311-a4f9-57177e01f2a7 | -21.70345 | -42.29165 | 2024-10-07 03:40:00 | NPP-375D | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 3e1a67cc-6836-365a-a1fb-42f4571f4c43 | -21.70239 | -42.29719 | 2024-10-07 03:40:00 | NPP-375D | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| bf686794-78bb-36c5-ad65-16b751de0cf4 | -22.09384 | -43.08942 | 2024-10-07 03:40:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1604e012-ddb1-3c46-80d4-1582046594e3 | -22.09306 | -43.09343 | 2024-10-07 03:40:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5ed35457-512a-39b9-82d2-52088c7ae98c | -22.06406 | -43.08664 | 2024-10-07 03:40:00 | NPP-375D | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 36eba866-e8d7-3d33-91c1-4e5e62940184 | -22.03247 | -42.88863 | 2024-10-07 03:40:00 | NPP-375D | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| dba18e96-36d4-30e7-8c75-e5576681d4d7 | -22.02841 | -42.88749 | 2024-10-07 03:40:00 | NPP-375D | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 8746fec5-c2bb-3ef6-803e-83b13e79b012 | -21.8075 | -42.51562 | 2024-10-07 03:40:00 | NPP-375D | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| cdee6e71-cc63-3917-90bd-d4c65f67d690 | -21.8042 | -42.51088 | 2024-10-07 03:40:00 | NPP-375D | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a27daeac-b387-3cd4-bf02-d9c254ca915e | -21.80019 | -42.50985 | 2024-10-07 03:40:00 | NPP-375D | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 68c051f0-0a76-3347-bb5a-613c5d9dfd5e | -21.78701 | -42.49088 | 2024-10-07 03:40:00 | NPP-375D | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 24ea04a2-4937-3ff7-8376-cb4e50e84039 | -21.78631 | -42.49456 | 2024-10-07 03:40:00 | NPP-375D | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ce73be4e-7420-38eb-bc61-fb8f87459d5b | -21.73686 | -43.02216 | 2024-10-07 03:40:00 | NPP-375D | GUARARÁ | MINAS GERAIS | Brasil | 3128501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2b06d868-0089-34a2-a5ee-810fd2d1193d | -21.73651 | -43.02372 | 2024-10-07 03:40:00 | NPP-375D | GUARARÁ | MINAS GERAIS | Brasil | 3128501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 523018ea-6e14-3925-89cc-8456e1ab7745 | -21.73236 | -43.02273 | 2024-10-07 03:40:00 | NPP-375D | GUARARÁ | MINAS GERAIS | Brasil | 3128501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4c29e7e1-9d67-3b9f-813f-4ddd7ca7e289 | -22.90247 | -43.75299 | 2024-10-07 03:40:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9dfa8bd6-93e3-3e57-a8e1-c28f10401f13 | -21.95617 | -45.37693 | 2024-10-07 03:40:00 | NPP-375D | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 44.1 |
| 3938a1ef-6487-3d1e-bb26-51e9bc47a586 | -21.95253 | -45.37033 | 2024-10-07 03:40:00 | NPP-375D | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 3d75c977-69c9-3fb2-be92-4adb0e34386f | -21.95145 | -45.37543 | 2024-10-07 03:40:00 | NPP-375D | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| b9317c62-747b-3e0c-b088-6ceb78e66c1b | -21.94899 | -45.36333 | 2024-10-07 03:40:00 | NPP-375D | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| cc774213-3e13-3ac4-9388-be7bf8bf6f2e | -21.6809 | -43.9812 | 2024-10-07 03:40:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b3aea288-c0f2-36a6-b965-ef97687af6e7 | -21.67995 | -43.98587 | 2024-10-07 03:40:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 00266eb3-72f6-380d-bcbd-4bda286241ed | -21.67269 | -43.99893 | 2024-10-07 03:40:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 97da884f-2f92-30b0-84bb-3ac78506544a | -21.67174 | -44.0036 | 2024-10-07 03:40:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 31c9b4b8-5d84-3aa6-a4f2-ae5326d9278d | -21.67078 | -44.0083 | 2024-10-07 03:40:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| fbf7ef78-8fa9-3bf0-9c20-bfa1c124384a | -21.66732 | -44.00259 | 2024-10-07 03:40:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 9216a0b2-8c4c-3a95-890a-9c00f3b71fa9 | -21.66636 | -44.00731 | 2024-10-07 03:40:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| e90ce175-ef13-386c-83c0-02ff13c790b6 | -21.66534 | -43.99841 | 2024-10-07 03:40:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cf4e43b3-de69-36a0-8b99-0abae9d978b2 | -21.66441 | -44.00318 | 2024-10-07 03:40:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 606f4d8d-97ed-3228-986d-4b1afabeb49a | -21.66388 | -43.99678 | 2024-10-07 03:40:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 27fc283b-4db4-3d7d-b4c9-9a57fe942557 | -21.66291 | -44.00154 | 2024-10-07 03:40:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3f1b8c95-e9ee-3a6f-8e87-ed1f6fa0baa0 | -21.53364 | -43.97586 | 2024-10-07 03:40:00 | NPP-375D | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 01d0c325-5ac6-347a-b20d-f53d0ae27252 | -21.40343 | -45.34609 | 2024-10-07 03:40:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| fc9c45c0-2008-38ca-8575-4d2e05032339 | -21.39858 | -45.34506 | 2024-10-07 03:40:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| c3c690df-0ad9-3274-b928-b6add5be9767 | -21.38976 | -44.27058 | 2024-10-07 03:40:00 | NPP-375D | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e56115fc-e09e-36ff-a87b-d5440350d65a | -21.38964 | -44.27263 | 2024-10-07 03:40:00 | NPP-375D | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b5c4afe9-5d46-3b4f-8468-f06094450af9 | -23.16219 | -45.55033 | 2024-10-07 03:40:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7ec88a9c-18eb-3abe-95f4-12851bdf9faa | -23.16103 | -45.55587 | 2024-10-07 03:40:00 | NPP-375D | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| bd315a87-f25a-3123-8be6-f34f3ca872b5 | -21.78738 | -46.41811 | 2024-10-07 03:40:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b2960e98-c6fb-3abf-9010-17fd9d4dc931 | -21.78669 | -46.42136 | 2024-10-07 03:40:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 178fce0e-8d15-3324-90f9-5c3b09b9c4dd | -21.57837 | -46.63161 | 2024-10-07 03:40:00 | NPP-375D | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 912b94f7-a26a-32b9-a75a-4c6b11b0f43b | -21.57755 | -46.63534 | 2024-10-07 03:40:00 | NPP-375D | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 147d8c1e-4103-3015-996b-75dc899594a6 | -21.57223 | -46.63459 | 2024-10-07 03:40:00 | NPP-375D | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 49b9e362-e8bd-321b-8a5b-abd2646415f3 | -21.57302 | -46.63097 | 2024-10-07 03:40:00 | NPP-375D | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fd1549a3-f287-359f-a58e-9bfd972e2a23 | -21.12357 | -46.62016 | 2024-10-07 03:40:00 | NPP-375D | SÃO PEDRO DA UNIÃO | MINAS GERAIS | Brasil | 3163904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2da4b8b8-ed59-3eb0-bd24-bf20465122d4 | -21.49484 | -45.69516 | 2024-10-07 03:40:00 | NPP-375D | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| aabd1f6c-3615-3e55-9e14-979b900a3cab | -21.40221 | -45.35191 | 2024-10-07 03:40:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d7c2cffe-0996-39ad-8a1b-7507db70fda2 | -21.39738 | -45.35073 | 2024-10-07 03:40:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 4abf6ad5-12ab-3ec7-8b65-3e79369361b0 | -21.14696 | -45.8251 | 2024-10-07 03:40:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| efb7e764-87cf-3d2f-8358-53cbc7f58d9e | -21.14631 | -45.82823 | 2024-10-07 03:40:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e5cfbee0-0a45-342f-ac1c-f28b82a976e3 | -21.14566 | -45.8313 | 2024-10-07 03:40:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 29c712f4-4228-352f-ad05-9e922c40412c | -21.1419 | -45.82419 | 2024-10-07 03:40:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bee3c22c-9554-3097-ba1c-2e3c5359ed98 | -21.14125 | -45.82729 | 2024-10-07 03:40:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4bb56e62-c3db-320b-997f-377092d6408a | -21.1406 | -45.83038 | 2024-10-07 03:40:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bfb4da93-6b07-3f78-b6f8-5cc2b1496b6a | -23.43934 | -47.05428 | 2024-10-07 03:40:00 | NPP-375D | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 6f8c4293-b6ad-36b4-a29c-5b0f879f31e8 | -23.43854 | -47.05785 | 2024-10-07 03:40:00 | NPP-375D | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| a1785c86-3950-348f-96b1-603624d48cef | -23.43774 | -47.06145 | 2024-10-07 03:40:00 | NPP-375D | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 971a9f3e-1150-34a7-b307-f03390798295 | -20.5145 | -48.12466 | 2024-10-07 03:40:00 | NPP-375D | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b1a4c9b3-5c0d-3980-9312-c12f3d5c87dc | -20.51353 | -48.12896 | 2024-10-07 03:40:00 | NPP-375D | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 20.2 |
| dbe579e8-aaea-3f9c-8889-861ca4b24259 | -20.51257 | -48.1332 | 2024-10-07 03:40:00 | NPP-375D | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 86f4cc74-2286-3061-beac-493470d3f735 | -20.50869 | -48.12318 | 2024-10-07 03:40:00 | NPP-375D | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |


[Clique aqui para ver as próximas entradas](README49.md)
