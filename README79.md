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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f31416c5-d446-3f54-bd25-7feadd31a349 | -12.14277 | -50.05783 | 2024-10-01 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| dbcdf931-1cf8-3bdc-87c7-a605449a3610 | -12.14207 | -50.06176 | 2024-10-01 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 2be4e002-4510-3fd5-9ca0-38323096f627 | -12.13928 | -50.05313 | 2024-10-01 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b307116d-0264-35a6-b119-5b3c79d10282 | -12.13859 | -50.05705 | 2024-10-01 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 60abe13a-c290-3843-a48e-91e3fc662109 | -12.13789 | -50.06098 | 2024-10-01 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93011ba3-de21-3a81-8bec-2c96f19bddae | -12.13718 | -50.08924 | 2024-10-01 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1df53afe-5f15-3dc3-818c-3b4b68ef01d7 | -12.1351 | -50.05235 | 2024-10-01 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5894330a-5426-3e98-a925-47463d9ac033 | -12.13509 | -50.07665 | 2024-10-01 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d7725d5-3da0-3d37-b785-92a2e3bc35b1 | -12.13369 | -50.08452 | 2024-10-01 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2557d8a-f9cb-34ed-b8b2-c9ab1dd211a8 | -12.12395 | -50.04218 | 2024-10-01 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c884967f-6a55-30e8-aee8-23dcae21284f | -12.09709 | -50.0184 | 2024-10-01 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cc776ee8-13a8-36ba-b90a-2c83b736cd6d | -12.09405 | -50.01642 | 2024-10-01 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b16ea80f-e1a3-398e-acfa-639c553c9f18 | -11.98517 | -50.30707 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 673df271-df37-353d-8579-41741133ac29 | -11.72542 | -50.00868 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57717434-2fe6-3a7c-83a6-000a582081f1 | -11.1574 | -49.72735 | 2024-10-01 04:14:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27eea701-597c-34f0-801d-8f3df7f42c78 | -11.15673 | -49.73123 | 2024-10-01 04:14:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ce64635-0811-3978-90af-a09cb0eadd02 | -11.13046 | -49.61169 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b58cc43-0be3-342f-9ff3-54c5c7c608a4 | -11.12633 | -49.61092 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22791ede-dc0e-3314-b41f-ffb568bc5ed3 | -11.11326 | -49.61241 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7c758a7-5166-376b-82bd-1970523484e9 | -11.11258 | -49.61624 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf88b3f5-7f28-391a-98e0-717d6fc1e44c | -11.11048 | -49.60402 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 830679cc-a8ea-3503-af16-aef76c70902a | -11.10702 | -49.59948 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f15951fe-435b-3ccd-b59e-116b38447b03 | -11.10634 | -49.60327 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f0981ef-6dc4-3a59-8f54-b64cb59c1b0d | -11.10356 | -49.59494 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7664aaf-9175-3c2f-ba9f-497603539c33 | -11.10288 | -49.59873 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83a78625-4921-349d-a63c-add7edae5391 | -11.10221 | -49.60252 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2998c3c9-c508-30bf-be90-08617dea64c7 | -11.1001 | -49.59041 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e76df10b-fbd1-3643-9a68-28502625cf46 | -11.09943 | -49.59419 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a955d93b-853c-365f-a6ac-a72fabd9e47a | -11.09875 | -49.59798 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a9ced36-7ced-3c4b-b695-02136ae11661 | -11.09597 | -49.58966 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68af0709-18ac-3897-b4f4-d5323ce61941 | -11.09529 | -49.59344 | 2024-10-01 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72980f94-c973-3fa4-a8e0-22fc22292b37 | -10.9845 | -50.16191 | 2024-10-01 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b79dd483-996c-3f05-b556-7ec2de57dfc0 | -10.98199 | -50.1635 | 2024-10-01 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7e51b4a4-54eb-34a2-ae8b-6a89b43e8a76 | -10.9802 | -50.16112 | 2024-10-01 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7b420989-4c9f-343f-97d7-d34d0fbb071b | -10.97945 | -50.16526 | 2024-10-01 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 29b6c9d2-06d0-3d07-adb3-e06dcb3c6b97 | -10.92426 | -50.08894 | 2024-10-01 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e81d30a3-aa3e-336f-91d1-d4685245329c | -10.92352 | -50.09306 | 2024-10-01 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7503bcc0-9f74-325d-a7e9-3d624d484184 | -10.91998 | -50.08816 | 2024-10-01 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 99dc3f70-df24-33bc-b569-79f75f79e4ab | -10.91924 | -50.09227 | 2024-10-01 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e0afab73-06e0-3b5f-afff-5f8cfc81754c | -10.91851 | -50.09637 | 2024-10-01 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e717cdee-9b92-3643-a739-f83cbce15607 | -13.66115 | -50.35101 | 2024-10-01 04:14:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c6343ed-f192-3bc7-a15c-dd5a8e14d4af | -13.65973 | -50.35872 | 2024-10-01 04:14:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ffad3c70-214a-3833-bec4-b6a96281da26 | -13.65964 | -50.3527 | 2024-10-01 04:14:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60a5accf-ca7e-341f-80b7-492398144a44 | -13.65616 | -50.34807 | 2024-10-01 04:14:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f97fe568-ea63-3a83-977a-434c2eb532f2 | -13.65547 | -50.35192 | 2024-10-01 04:14:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf0226a5-ef8a-3a14-ad01-8bcfb42957a3 | -13.65063 | -50.35501 | 2024-10-01 04:14:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88149629-df6e-3274-93e1-89297792f658 | -13.64994 | -50.35886 | 2024-10-01 04:14:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ec09e185-03a2-3c74-b15f-b7a3d402b084 | -13.64715 | -50.35035 | 2024-10-01 04:14:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 695f274a-2730-3e13-a72e-6a292a95087b | -13.64647 | -50.35422 | 2024-10-01 04:14:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac42c0e5-98f4-36e2-9591-7dc2fbf50e11 | -12.41504 | -50.96184 | 2024-10-01 04:14:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c8f14d44-b991-39b0-a32c-4986a1255305 | -12.40981 | -50.96544 | 2024-10-01 04:14:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f060bcbd-1241-391e-b123-501e02a24a68 | -12.40377 | -50.97348 | 2024-10-01 04:14:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b13e56ef-87ff-35d2-8312-de8125704a62 | -12.39854 | -50.97708 | 2024-10-01 04:14:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8be05472-6e93-3435-b3e5-c7bd4a99b84d | -12.28154 | -50.64736 | 2024-10-01 04:14:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 68f08ec2-5ec6-33b4-a211-78d66ebe82b9 | -12.27657 | -50.45132 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ddcd582-241b-36c4-ba42-7a423df9e561 | -13.64368 | -50.34571 | 2024-10-01 04:14:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1bd92a84-9538-36e7-8766-c38e03cc4de8 | -13.64021 | -50.34104 | 2024-10-01 04:14:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 038c2c7c-a650-31c7-80f6-6fb7e3647193 | -13.63744 | -50.33252 | 2024-10-01 04:14:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3b7e4a1-f8d5-3f72-9fbd-07245c35b611 | -13.63675 | -50.33638 | 2024-10-01 04:14:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d0a76df-72e7-38b1-b25a-85492e24e2f1 | -13.64387 | -51.10303 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 114957bf-1872-3ca9-a1af-feeda869c4e0 | -13.64334 | -51.10422 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 713d11f5-b698-3c39-971e-803858153070 | -13.64306 | -51.10737 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b615fbe3-ed0c-3a55-9127-538ec5a83ce1 | -13.64256 | -51.10857 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 439c963c-ad60-3bb3-bfd2-3d09b83d0a85 | -13.63897 | -51.10336 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1493e626-bcee-3611-b8e8-d0592c1e15af | -13.6387 | -51.10652 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 19938336-2bda-3a69-8aa0-ca55d41680fd | -13.63819 | -51.10771 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 84790fe9-9618-3f87-b0b6-f2830e023cc5 | -13.63515 | -51.10133 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| ffbc0274-44e5-3e69-9d25-720ce17a4224 | -13.6346 | -51.1025 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| f10bea5d-6470-3158-ae84-63afe5ae6072 | -13.63433 | -51.10567 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 8e6c3065-c3f9-3b7b-b794-310fcf7a2daf | -13.63382 | -51.10686 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 1b1e2f5b-4b38-3204-819f-b6ce082fd7d9 | -13.63352 | -51.11002 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4f32c3e7-cee6-3ba3-8b38-0e9efb331521 | -13.63304 | -51.11121 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 01299f2f-0cbd-36ab-997b-d3f6b2a74bc9 | -13.63102 | -51.0973 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| a3373ad3-e039-3cfc-ab4d-e0c6a09ed7da | -13.63078 | -51.10049 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 7aea3c6a-bdff-33a9-b8e6-cd6f6878c985 | -13.63024 | -51.10165 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| deb84a15-561b-39dd-99a7-56bbac7325a8 | -13.62996 | -51.10483 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| fc930600-cd93-3cdc-9718-b416933b224f | -13.62945 | -51.10601 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 63d43556-98f5-3bfa-a390-4c3d583303e4 | -13.62915 | -51.10917 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 373c5624-92c7-3e6e-8352-3075c3fd3608 | -13.62867 | -51.11035 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b7696f84-7912-3c3b-bd74-9ba5e68b95eb | -13.62666 | -51.09645 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| de28cc71-0f35-3f73-975e-6cc134fa71f4 | -13.62587 | -51.1008 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 700778cd-2eb7-3fd3-8743-d468f006f616 | -13.62509 | -51.10515 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| de4804d6-c03c-3658-9ebc-f44eac04c56f | -13.62229 | -51.0956 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a9ed2770-75c5-3288-bfc2-455662e2b01d | -13.6215 | -51.09995 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3d59b982-3f1a-36c8-bf2f-37e996f531b9 | -13.61792 | -51.09475 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e62cfb2a-49fb-3b4e-8e23-968f3d02c6da | -16.09392 | -50.33626 | 2024-10-01 04:14:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 67d396d8-6dff-3ba1-8174-99b5d136d1f4 | -13.61435 | -51.08955 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4f05edfe-b5c8-3d03-adfa-10d552ee18cf | -13.61356 | -51.0939 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1b8c2ba1-b70b-3c0b-81d9-374230ecf393 | -13.60998 | -51.0887 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ae9e02b-bf9f-3405-94df-6703d89ca903 | -13.60919 | -51.09305 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1271210d-5cd9-38e7-92f8-cbaf618bf912 | -13.60641 | -51.0835 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f52c3b00-f3ee-3f5e-ba0f-ce5853f2f170 | -13.60562 | -51.08786 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1dc80678-b787-3e56-8cda-d72200662ca0 | -13.60284 | -51.07831 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e64af52f-f56f-3e7f-b3c1-576eb689ff33 | -13.60205 | -51.08265 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 415c5fc0-1be8-3cbe-96d5-f06096127f31 | -13.59926 | -51.07313 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 43d1595c-8f7b-3e67-89da-f11e96673fb3 | -13.59847 | -51.07747 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6c248d5-e5d6-32aa-889d-7aef941121de | -13.59569 | -51.06796 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60aa01b2-b5f2-3afd-8af8-bd442ef96cd5 | -13.5949 | -51.07228 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac7e0bf7-b286-3be7-a998-1db4a5e7a98d | -13.59133 | -51.06711 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 358a459c-f70b-3874-ad15-c7495dbea3a2 | -13.58341 | -51.0611 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README80.md)
