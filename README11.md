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
| 4a4e1242-6f56-34c7-babf-bf098c351a49 | -12.3691 | -49.98935 | 2025-05-27 04:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27804470-5a80-3edf-8d07-481888adac5e | -12.83088 | -47.38266 | 2025-05-27 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e56c388-7f1c-3f10-bbea-2973e51ca837 | -10.84444 | -54.02232 | 2025-05-27 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4966a06-f89e-3ecd-bff4-8ae30a45d33d | -10.82022 | -56.96012 | 2025-05-27 04:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92002399-5b49-3c15-b8f4-8bc83dd673ce | -15.17342 | -52.29251 | 2025-05-27 04:29:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d72aed4-1b21-324a-8ac6-bcdd54de231f | -12.83421 | -47.38321 | 2025-05-27 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b7fefd0-3615-3870-a3e5-ed14751c5d5c | -14.04089 | -55.13364 | 2025-05-27 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d75274bf-6126-329f-b691-fb411d4767f1 | -14.65718 | -45.08881 | 2025-05-27 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24599c93-5ee8-3f9a-a7c5-ff0306c79397 | -10.81591 | -54.02645 | 2025-05-27 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be90b75c-0532-3a1f-9fb7-645c922eeb76 | -11.14038 | -53.92486 | 2025-05-27 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2e48ca50-fe16-39a5-962e-02316cf8707d | -13.3793 | -48.72767 | 2025-05-27 04:29:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e2e7e61-9414-30e7-8769-8068ab9b39c0 | -12.03946 | -51.59515 | 2025-05-27 04:29:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 590d932e-71bd-30e8-bed5-ca3703ba1aaf | -12.42107 | -49.97823 | 2025-05-27 04:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e5e1c63-8768-3e9b-8489-1e136fadb5ea | -15.25331 | -47.46959 | 2025-05-27 04:29:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 329ebfc8-1910-3f7d-9b68-80d88d17215d | -12.11533 | -54.66422 | 2025-05-27 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a49ebe9c-8171-3280-ae71-990262284f33 | -12.12449 | -54.66594 | 2025-05-27 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2019dd22-f280-3d6d-bc00-eafd92a00cd8 | -13.78315 | -54.31668 | 2025-05-27 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 122a59fd-5c80-368d-909e-807ae1f8a959 | -15.88138 | -43.45708 | 2025-05-27 04:29:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 9b4aee6b-190c-395c-8b5a-2da80ed1ef4d | -15.16966 | -52.29185 | 2025-05-27 04:29:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 395d79c3-bc90-3565-9771-cfed237b5f7d | -17.2336 | -46.7873 | 2025-05-27 04:29:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 085b6c4b-8a8d-3d10-8c30-f05e0b44302e | -13.20925 | -48.91805 | 2025-05-27 04:29:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f713c16-d01e-3a83-8504-cdff604c34d3 | -11.62277 | -54.9412 | 2025-05-27 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 59b90d5f-929a-3c88-bbf9-ae67ae52abec | -12.64486 | -54.08153 | 2025-05-27 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f29a119f-6adc-3448-9dd0-9c27afc2f1d0 | -14.01913 | -55.12763 | 2025-05-27 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49cf518b-386c-3fc9-b16f-4432e20c6a27 | -14.01457 | -55.12672 | 2025-05-27 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd3c22a3-41e5-36f3-b475-76aa2e58dc93 | -16.64012 | -51.52507 | 2025-05-27 04:29:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04c0e291-487a-3b2c-890d-93ee278ed065 | -12.82865 | -47.39688 | 2025-05-27 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f6b31f1e-c9f3-3f71-88aa-d12598f831cb | -12.07586 | -47.34832 | 2025-05-27 04:29:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 179a80fb-d5e3-3f30-880f-8358169245ab | -12.35579 | -49.919 | 2025-05-27 04:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9fcae5ad-6500-3d75-a567-1d85416601c3 | -12.07531 | -47.35186 | 2025-05-27 04:29:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ce0c31ab-b490-39e4-ba59-61d0b97994e3 | -12.8281 | -47.40043 | 2025-05-27 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31becbb3-5b21-3a75-8726-22aeb094ed13 | -12.65739 | -52.43889 | 2025-05-27 04:29:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e2b0ba7-e7e3-3133-b386-2611f6925fe0 | -12.6405 | -54.0807 | 2025-05-27 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab3efb4f-6489-3c27-9943-cdf12d78bd14 | -12.82476 | -47.39989 | 2025-05-27 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 85e73b85-5e6d-3abf-89f9-88ee70b600bf | -12.82754 | -47.38213 | 2025-05-27 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f545da10-5d91-32fd-bc63-e639a184bbd7 | -12.07808 | -47.35593 | 2025-05-27 04:29:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 210c750e-a60c-35cc-9edd-71e406b091a3 | -12.35514 | -49.92286 | 2025-05-27 04:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3265a15-e9cb-3697-9500-72ff2a4cedbe | -17.64906 | -47.45963 | 2025-05-27 04:29:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b9409dac-a879-35a5-9d88-670603e876f2 | -12.37391 | -47.32005 | 2025-05-27 04:29:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4c118d0d-1373-3c3a-bf79-d0fdc2b6c078 | -10.82121 | -54.02269 | 2025-05-27 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5577929c-a92e-3b33-aaa4-0919d12629f9 | -15.24996 | -47.46904 | 2025-05-27 04:29:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6135ad19-6b9e-378e-867a-0e61400f23ee | -15.80477 | -43.57043 | 2025-05-27 04:29:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6f8dd963-c664-3a35-845b-e5332a79dfda | -15.88541 | -43.45767 | 2025-05-27 04:29:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 20.3 |
| c2d79088-900d-3782-b472-6f77c20848a7 | -14.14845 | -45.47428 | 2025-05-27 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 731a553a-a76b-3878-8aa3-ca5665871d74 | -14.14139 | -45.47319 | 2025-05-27 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8cc8cb87-f6b6-3e65-bcaa-ddcef83a9003 | -15.80078 | -43.56984 | 2025-05-27 04:29:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 64e59cd8-90b8-332a-821e-f40ba63e0bb8 | -10.29916 | -57.14452 | 2025-05-27 04:29:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a32a4a1-fb12-3644-af08-3206e82c7426 | -14.01827 | -55.13233 | 2025-05-27 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e421aa0e-209b-39d2-b079-f61289a72534 | -12.83032 | -47.38622 | 2025-05-27 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a418a99b-e645-31d7-8472-ebe2f0b9c660 | -14.14786 | -45.47832 | 2025-05-27 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ca9b112-334c-305c-ba08-3ea07d96f6a5 | -14.0309 | -55.13644 | 2025-05-27 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a9a2ace-cb8e-363c-963b-1f537d5a1eb1 | -14.0163 | -55.13851 | 2025-05-27 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b670de65-4b7e-30e2-965f-b1b2c5662c4c | -11.81885 | -55.07675 | 2025-05-27 04:29:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 158bc3a8-d1a4-3a1a-b988-cb245755e771 | -11.40437 | -52.95755 | 2025-05-27 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c9fc2e6-b37b-36b6-8aaa-22fc4ff91196 | -14.63578 | -47.94209 | 2025-05-27 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6225d24d-e618-398d-b61a-22a81c5354e0 | -12.25075 | -51.44444 | 2025-05-27 04:29:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba63ecc4-3e10-3847-8c5f-e26a3e5f97e1 | -10.29427 | -57.13976 | 2025-05-27 04:29:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c6d9619-fa5e-3a08-9a89-0db6970a784f | -12.11447 | -54.66895 | 2025-05-27 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 061e1d74-ed3a-392b-8221-ec0e0d2724d8 | -14.23902 | -45.66764 | 2025-05-27 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 703ef059-5585-365b-ab12-0719f81783d9 | -10.82637 | -56.95746 | 2025-05-27 04:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c21b297-7520-3ffa-b762-35041cbe9027 | -12.41978 | -49.98606 | 2025-05-27 04:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f72e94b-51cf-305b-b9a4-3fc82c0f7890 | -16.13801 | -53.02069 | 2025-05-27 04:29:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a597c0d-bcab-3e89-8c82-1cf2d54d4fe0 | -14.01654 | -55.14177 | 2025-05-27 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27c18b1f-9b16-30ab-8f50-c363a947d3e8 | -10.8204 | -54.02725 | 2025-05-27 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da792f7d-b677-3c1d-ba96-96dc56428000 | -14.04178 | -55.12896 | 2025-05-27 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 20efcca5-0d88-3e4a-8c95-86f69236c9c1 | -11.14118 | -53.92046 | 2025-05-27 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| deaf8fab-331f-37cb-a2ce-8acc6a6c2812 | -14.66079 | -45.08936 | 2025-05-27 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ffa6c6c-aea0-342d-8dcf-cc1999e54de1 | -10.29358 | -57.14351 | 2025-05-27 04:29:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 574aa414-50a1-3d36-b50d-dc19b34a43a1 | -10.8257 | -54.0235 | 2025-05-27 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8890caef-cb97-3393-b4d6-4b926c7bb6d4 | -14.02723 | -55.13084 | 2025-05-27 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 814ab529-c049-3117-a113-4833a44d8e76 | -14.02087 | -55.13939 | 2025-05-27 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb9ab04f-9bf5-3bbd-8c69-41ba0b73477f | -11.13594 | -53.92408 | 2025-05-27 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 33a59b4d-2bbb-3fe6-a99b-a312b1327631 | -14.59443 | -48.35634 | 2025-05-27 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cc3b4e6-55aa-3e0a-a0dd-39a0dccb5c6e | -12.07198 | -47.35131 | 2025-05-27 04:29:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 713127f2-f08b-352d-8df6-c060e1472d20 | -14.02634 | -55.13555 | 2025-05-27 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f0b5435-1a38-3c5f-bceb-84db2ddc8f74 | -11.13674 | -53.91969 | 2025-05-27 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b82fc93c-a82d-3b6c-93aa-eef9bd913cfe | -12.82699 | -47.38568 | 2025-05-27 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1821d437-ad37-3a5a-b842-d7fd8ef25b8f | -10.81754 | -54.01733 | 2025-05-27 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7023931-c5f9-372b-a1cb-cba20e939531 | -12.65607 | -52.44051 | 2025-05-27 04:29:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8dfc454-6e57-3056-b95d-bc14dcd69068 | -12.06865 | -47.35078 | 2025-05-27 04:29:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 398aa2bc-ab1b-3c5b-908a-86fd409bb027 | -10.81673 | -54.02188 | 2025-05-27 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0beab0d-07da-3a96-a952-96835a63fab4 | -10.82569 | -56.96104 | 2025-05-27 04:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8a805ef-55ad-35c0-8c05-0f18d668f200 | -12.17035 | -54.26003 | 2025-05-27 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5b299d2-5e23-3683-94d9-b1167a54f3ce | -12.37258 | -49.98995 | 2025-05-27 04:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58d9b9ed-5c6c-329c-883d-f36863d1b96e | -10.29827 | -57.13976 | 2025-05-27 04:29:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2c6b3fd-26c5-31da-9676-c82d7ecad9f4 | -15.8859 | -43.45408 | 2025-05-27 04:29:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 20.3 |
| d0aa82ea-1e1e-3ed2-89f9-1b4e4d118feb | -10.84525 | -54.01776 | 2025-05-27 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78744941-f51e-35c0-a92b-552736e730dc | -12.35231 | -49.91841 | 2025-05-27 04:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6cf214aa-a4a4-3461-acdd-578a0e144a15 | -14.62468 | -47.94757 | 2025-05-27 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b53ad662-4cfa-39ee-86d3-3edb655826bd | -14.14492 | -45.47373 | 2025-05-27 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a4466cd-3fd2-3876-bee6-ddfccae96976 | -14.01543 | -55.12206 | 2025-05-27 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c1b0979-3de2-3320-a28a-be83c0699359 | -14.80505 | -48.26271 | 2025-05-27 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0034fb8a-b454-3a2a-8cb1-42580f9879ef | -14.01443 | -55.12355 | 2025-05-27 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 69905afd-ba1c-335b-9532-58850ee05f72 | -15.88187 | -43.45349 | 2025-05-27 04:29:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 4da0ab09-ca7e-300f-9ae1-ebf172561732 | -11.40092 | -52.95295 | 2025-05-27 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8025ce96-d298-3196-9865-dec553a2c18a | -10.82937 | -54.02893 | 2025-05-27 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e841b9c-5805-38ea-90bc-b8bbff0d681b | -10.82704 | -56.9539 | 2025-05-27 04:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| caf2c992-b6f7-301d-8542-c44ebf1f0a2d | -10.84605 | -54.01322 | 2025-05-27 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fca2ec2-1b14-3c4f-8d8b-8e0a058034a4 | -15.07973 | -48.94495 | 2025-05-27 04:29:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9381d4cb-f7ae-39da-9aed-c13fa9291074 | -16.68196 | -43.88348 | 2025-05-27 04:29:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README12.md)
