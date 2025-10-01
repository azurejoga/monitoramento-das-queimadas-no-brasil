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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c7c04bd-9519-312d-8fd2-ada91717d12c | -7.85674 | -54.97351 | 2025-10-01 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc339c26-ea67-3ccf-9b07-10e3f0aba389 | -12.69675 | -48.56395 | 2025-10-01 05:10:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b3eb64f1-46c0-3349-87a3-37663d74c023 | -12.81707 | -47.01867 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 882d709f-1c0f-31c2-b76c-dd64c5e412a5 | -8.54969 | -44.64385 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0bc82d0b-6b83-3800-b1ce-82a5ebcfcbd1 | -11.46437 | -45.0103 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 077f3a46-56dc-3d3a-a66e-08783db1f10d | -10.04036 | -52.10356 | 2025-10-01 05:10:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b6e8791-c238-37d8-8c81-12d820c619dd | -13.24052 | -47.33196 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9931220e-8b41-3202-b51b-566e2086cb86 | -12.42525 | -50.18273 | 2025-10-01 05:10:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe0b0aac-2a3f-3619-b36d-010509eb314c | -6.79918 | -44.74977 | 2025-10-01 05:10:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 116f3dfd-f8da-362d-b6e8-81ccbfb2743c | -11.47095 | -45.07765 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce294e26-fd5b-323b-8e0c-2f32cc43fdc2 | -11.75546 | -46.83973 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dc33b2c7-0fcb-3813-a1e4-55e642693eb8 | -12.84117 | -46.86798 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7fc821d2-7769-37ae-aec6-010a10a53be9 | -13.33567 | -48.14735 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7fc790d2-e5fb-3501-a414-29b02e07fd22 | -11.84898 | -45.01793 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a30234d-925c-3f0e-b558-0d419dc98c48 | -11.2773 | -47.81157 | 2025-10-01 05:10:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb1d1528-e486-3e82-ba0c-d14959621983 | -8.55495 | -44.76442 | 2025-10-01 05:10:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 08ade544-8aa8-35ff-ac09-a1bdc792aa96 | -12.20817 | -47.81163 | 2025-10-01 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79ebd6b3-5818-3796-95e6-3b422754349a | -10.78761 | -45.3622 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccb8f22b-e01a-3872-9231-6e761e4b28c0 | -11.83857 | -44.98487 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 43478cbf-a8e2-3820-b011-235912770c28 | -11.63373 | -47.49403 | 2025-10-01 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3c76c38-d8e8-3de9-a8ea-e3ecb448665f | -13.3235 | -48.14978 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7bc0c49-ee83-339c-bca1-b6c1f9ccbc65 | -8.88995 | -46.6284 | 2025-10-01 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8fd7017b-941b-385c-a6a1-8ee90f830377 | -8.89234 | -45.04919 | 2025-10-01 05:10:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1998ef66-ca07-362d-abc0-01f1bc12ca86 | -10.48471 | -49.36813 | 2025-10-01 05:10:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c4e87a5-5fda-3331-a79e-e382126c302c | -12.80357 | -46.89213 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97cda2fe-f1cb-3e1a-83fb-65ddd440fd8c | -11.18773 | -47.20585 | 2025-10-01 05:10:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab0a758f-5cf5-3376-af2e-46ebef1fbec5 | -10.04577 | -52.09599 | 2025-10-01 05:10:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36cb3fa1-54d7-3d5d-a4e5-e0f795c5021c | -7.05483 | -46.41919 | 2025-10-01 05:10:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4947f0e8-f9d8-3df1-98a8-5c9da25c6418 | -11.47567 | -45.0981 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b11917b-9726-346e-8616-48963ddc9c52 | -13.31091 | -47.20988 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9cbf6b55-88c3-3a13-b619-cf129371bf62 | -11.80421 | -46.61873 | 2025-10-01 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4ff378a0-c25b-3d35-bba1-26fde7945ed9 | -11.75343 | -46.84219 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8829c91b-2972-35e6-9894-6b7b1e7e83e1 | -11.56913 | -50.18489 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 47b55b03-d4b9-3650-ac59-ecf3c1e011aa | -12.87464 | -46.94136 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b7d2430-e9a6-334e-b592-67bc4473b761 | -10.47644 | -55.6236 | 2025-10-01 05:10:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d47eecc-9674-3b1f-b492-0d84e5427fc7 | -11.92205 | -47.89411 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4dc29202-7822-33e0-b8a9-4cd30291485f | -13.55707 | -47.27835 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3f0cca4-50c0-3260-95f0-f60bbb69fef0 | -11.79785 | -46.61824 | 2025-10-01 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1e1d1fcd-881b-3d62-a14e-24b1386c03ab | -6.90077 | -44.98087 | 2025-10-01 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b02efeee-df09-3dfe-acf6-f16f6cee641d | -11.1546 | -54.12244 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39f50271-d230-3aab-ab22-95f3332d717c | -11.04605 | -47.82059 | 2025-10-01 05:10:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f86f4a1a-64e0-3ada-97be-028a2723b1ad | -10.48656 | -55.58046 | 2025-10-01 05:10:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed0efe20-3f5f-3e2e-9109-dad0168b79d3 | -11.83815 | -48.05289 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0e7391d9-3226-3a9f-a993-72227a124135 | -11.67166 | -46.97108 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 4132d49c-51b3-33c2-b3ee-17bb8add24ac | -12.8679 | -46.94463 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7228a6a-56c8-3ce4-bd17-96d6db035416 | -13.12939 | -47.43293 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a64c5ca5-15cc-32f0-a1c9-bea1dc2f8214 | -12.8485 | -46.94728 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 79d3d3e0-a8ff-3bb9-b1fe-0faecf1884db | -12.87375 | -46.77865 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 863c7117-1a36-3c2e-b969-2b6178a30053 | -11.79511 | -46.61539 | 2025-10-01 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92482ebd-b2dd-343b-8bd3-1d39fef00d0e | -7.83575 | -48.19905 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c61c9656-73cf-3a96-869a-de98ef0564c6 | -8.85219 | -48.41804 | 2025-10-01 05:10:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46b89f97-40c5-36fb-9153-2a42f0eb5ee7 | -13.33689 | -47.8139 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e881f69-7375-3190-9764-7472097b4ef5 | -7.05008 | -46.40907 | 2025-10-01 05:10:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97921ec2-4a77-3bcd-9136-13f48e6cd08c | -12.24562 | -47.79911 | 2025-10-01 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 904ef8b5-295a-3eb1-a1d6-dd5b218ae0f8 | -10.03662 | -52.09891 | 2025-10-01 05:10:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| befc28c3-36b2-39fc-9a2e-3c3cb74dceb5 | -6.91478 | -55.45383 | 2025-10-01 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f109a4b5-7cb2-3e15-8eba-c633968258a5 | -11.83627 | -48.06889 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e7fe9c35-3d17-37d5-8bfa-6d92e65a1538 | -11.15528 | -54.11766 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e48508e5-186c-3940-86ee-073635b5a553 | -10.08709 | -50.19592 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b5160df6-8014-3d4c-8d5f-112e760b8413 | -11.76446 | -46.85649 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bd73741e-1018-3fd4-b7bf-883ff168de73 | -10.04147 | -52.09541 | 2025-10-01 05:10:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f7762fd-67c8-30ea-8661-051bd590b970 | -6.79253 | -44.74875 | 2025-10-01 05:10:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77f83032-977a-380a-ab92-071afa59ee40 | -12.62074 | -44.86948 | 2025-10-01 05:10:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 57846126-3aba-3ac1-bc9d-bcae35be87e1 | -11.74965 | -46.83533 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 85f261da-df2c-3949-8a29-06b4bad7c352 | -9.43205 | -54.71543 | 2025-10-01 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26c73143-b074-34cc-a054-8b18fc68b46f | -11.46579 | -44.99745 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 62170c0f-3845-303d-823a-6c3786098b2f | -6.5105 | -54.8904 | 2025-10-01 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9620d39d-b2c0-3f57-83cd-aefb7bd48d39 | -13.29365 | -47.23835 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8ea82be-2de4-342a-acaf-0ad80b6a880d | -10.63902 | -48.53185 | 2025-10-01 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f3e42ec0-e44e-3516-9c89-47dfa3369c6b | -11.76448 | -46.86989 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b19d8018-a79b-3d3b-93e7-4166a3337713 | -13.30463 | -47.20977 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 866d14f8-34b2-3525-9552-43495b054590 | -7.87077 | -47.28096 | 2025-10-01 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 33e362d5-7350-308b-892d-0d02f0d51df7 | -11.76641 | -46.85393 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e6c0d5f3-a10d-371b-a894-600c747699d3 | -7.39418 | -44.60564 | 2025-10-01 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bc1d3c5-3cd3-37ac-9841-1ddf219079e9 | -11.85646 | -45.01421 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3b381db9-16b0-333c-bc24-d0179ea668a5 | -9.35204 | -46.32948 | 2025-10-01 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 29a02c05-48c5-3c51-8e34-b9a648345bd8 | -12.43052 | -50.17264 | 2025-10-01 05:10:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c30af7c4-8c42-3914-9e91-e2d50c8bfde9 | -10.43574 | -50.86235 | 2025-10-01 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d7e6133-e1e2-36a6-ac98-46351315e07d | -12.28237 | -47.8289 | 2025-10-01 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45f12cc9-7b5e-3632-9f54-de97f8d32259 | -8.23207 | -45.51499 | 2025-10-01 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a2095f6f-5822-3e12-a173-d30531261360 | -13.35966 | -48.14559 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 690a9748-4720-3476-9eae-ed2afaab0e63 | -12.85286 | -47.02138 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 64d3e746-7531-300a-a179-1305cfff24fb | -11.46114 | -44.97572 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 322d9117-5175-30e2-9b7d-b3765c3b7efd | -13.34789 | -48.14444 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1bdd20fb-543d-388b-b1bc-d1adffe7e277 | -11.16677 | -54.11927 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b536d7a-be0d-3688-9a37-97fdd085c595 | -11.46658 | -44.99738 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5dbbaa9-84fe-32f4-ade2-7e81dba86d6c | -11.09368 | -47.72205 | 2025-10-01 05:10:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7bf48528-c9bc-3caf-b424-95b43f61f2df | -7.26264 | -48.47766 | 2025-10-01 05:10:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ca30c04-c7ac-3a02-93e8-eb71b824bb38 | -9.85166 | -44.60719 | 2025-10-01 05:10:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 917a8974-f52e-3b67-8322-58d1ebef3a80 | -12.82798 | -50.58135 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d54d18f2-d20f-388b-a2af-aed0c8509088 | -7.41178 | -45.41204 | 2025-10-01 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 208ae049-df24-3359-bc64-f4dc081bda74 | -7.14388 | -47.26875 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fc71a385-501c-3c83-a978-14dca6c9adbf | -10.80676 | -45.35376 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92c92017-98fd-321f-9334-abf2ebf893e3 | -11.5866 | -45.04817 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 53c092d3-fe21-3064-97b1-ddd9a9f1ab17 | -12.85919 | -47.02149 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3da5ff98-c88f-3dd3-b381-adc0d829e655 | -8.88499 | -46.61872 | 2025-10-01 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 995460d4-d1e7-397f-b117-b393202b77f1 | -7.82301 | -47.0682 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88e66b7e-6572-3778-a7ae-b7827d872fb8 | -9.27548 | -57.16912 | 2025-10-01 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae7712f1-b691-3b62-a58b-5267fdfb3882 | -9.41241 | -47.33567 | 2025-10-01 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4427196d-e04b-3b96-998d-79e145debc41 | -11.15011 | -54.12666 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README124.md)
