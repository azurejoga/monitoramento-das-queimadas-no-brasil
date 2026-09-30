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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7d9662f-ba71-30c9-96c3-f053c1afebaf | -3.37519 | -50.94086 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f4b54254-818d-3841-aeb5-8e8cae2a91a4 | -12.12314 | -61.15164 | 2026-09-30 04:53:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9124784-0d8c-355f-a62d-0da672e046c5 | -8.26626 | -54.75103 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 584db462-3d98-378c-a32d-b904094f04f8 | -6.12956 | -57.78752 | 2026-09-30 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2def6ee9-a6e9-3d56-a297-061533cca6b7 | -12.77265 | -47.25718 | 2026-09-30 04:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 324c76bd-9ea9-3a2e-b0a3-5da3cf4550f8 | -12.78984 | -53.99507 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 300e63ae-7904-372f-b620-294203fa6ee8 | -14.20513 | -42.07448 | 2026-09-30 04:55:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b4422b0a-8d7d-3ae4-abbb-261726af04d1 | -12.77774 | -54.02669 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5b8b761-9202-3a4a-8b9d-ebf87658e685 | -11.51622 | -54.35392 | 2026-09-30 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be52e6b5-4a6c-315b-9318-31cd720242b2 | -13.52696 | -49.17746 | 2026-09-30 04:55:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d70a57b-1f8e-35e6-9a4b-076df9d1a9f6 | -11.81385 | -50.45652 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 84224dbb-6c89-3e86-aae0-d387bf11ccc3 | -11.54847 | -54.49973 | 2026-09-30 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 100673d6-2d03-3c0b-a20f-c087d88293c7 | -11.85073 | -50.97719 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bb5cc89-2c55-3d67-befd-544885d7c3bc | -11.37681 | -51.02347 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 162ca201-c970-3d35-9193-f8fa8551b0d5 | -21.38274 | -45.3133 | 2026-09-30 04:55:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f192121f-17df-3eb7-a22f-5d80ef0fcfc0 | -12.77677 | -54.01154 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6099e72-3473-342f-a3bc-7d34fa13fbb2 | -18.27472 | -53.0375 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4aaf16e8-56f7-3c81-aabf-d12e5e1a7185 | -12.7835 | -54.01268 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8e77d65-21ed-3827-b383-a2fedb13c3c3 | -11.3981 | -50.98589 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 026d1c68-0a43-398d-904a-2caa2f65acd0 | -11.36615 | -51.02551 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6cfd2a8-68a8-31c2-be1d-c8925b3f4279 | -12.79201 | -54.00291 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd914cfc-8b97-3745-8011-f3c65f961c58 | -18.50932 | -45.13566 | 2026-09-30 04:55:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f9c298f-2363-3164-b422-9ad2a60f3724 | -11.82701 | -50.46245 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61fcf3ba-776c-3424-8dea-71fbd62199d7 | -11.81042 | -50.45598 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 088641c8-aee6-30f3-88c0-8c26683fb826 | -12.07351 | -46.45072 | 2026-09-30 04:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 448611c2-d2cd-301c-b67d-43c8556a8fe3 | -14.01137 | -42.91027 | 2026-09-30 04:55:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| f3f05601-fa3d-345d-b1da-18789fbfce05 | -18.49767 | -45.14654 | 2026-09-30 04:55:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 441ca34f-c5b7-3a39-8e26-c0234e1b31d0 | -11.35661 | -50.97562 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cc152739-6fec-3e5b-82b4-9b16a813622a | -11.80985 | -50.45978 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e2a3057c-7503-3c87-8b3d-5544dd7b20d6 | -11.82072 | -50.45758 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c1aa5528-3b13-35c1-b9f2-5249f4b9fe74 | -12.44095 | -44.16947 | 2026-09-30 04:55:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b97b2b47-2b92-374b-9e4a-697b4f85635a | -18.26245 | -53.05055 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4a2af421-e620-312f-b9f0-b2377619625d | -10.898 | -56.17832 | 2026-09-30 04:55:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 013538fb-f466-3544-bc49-39d711ed7b4f | -13.53558 | -49.17005 | 2026-09-30 04:55:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90e0a3f4-02dd-314d-b09d-cc0e5e9d274e | -11.35101 | -51.03426 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7df4944-a813-3a07-b839-c4979cb6b5b5 | -18.29921 | -43.32941 | 2026-09-30 04:55:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 115dee6e-b46f-347e-b2fa-3c7d410fd174 | -12.05405 | -46.44629 | 2026-09-30 04:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee1af97c-f857-3f17-97ce-d9719ec61867 | -13.546 | -49.17655 | 2026-09-30 04:55:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86fd4bda-9af6-3fd6-aed6-9cbf9d9a72fd | -11.38466 | -51.01727 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3a9fd5c3-a3ad-3897-8e91-a29cfc173ade | -11.36166 | -50.98759 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98a5eddc-1134-3f43-80e7-a18b1c7d2873 | -12.7829 | -54.01632 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12961251-4f22-3856-83c9-b147e1d41adc | -11.81328 | -50.46031 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 23201fb4-75f1-3e5f-b91f-ae0840a3f6e4 | -11.80755 | -50.45165 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 2b38d963-f85d-3ff4-a5e6-f7aadff66687 | -11.38073 | -51.02037 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e08697a5-dced-36a6-baea-fb5d86238c08 | -12.78529 | -54.00176 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a61bf6ca-9129-3dd5-a059-76ef8f57f14e | -11.84932 | -50.47756 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec39ad99-49ca-3402-8697-64ae86359551 | -11.35438 | -51.03479 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3db6ba5e-4e23-3147-be51-1e53df188dbb | -14.01181 | -42.90646 | 2026-09-30 04:55:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 5b72302c-b44f-3955-beb5-aa5d665c00e9 | -23.00042 | -48.61556 | 2026-09-30 04:55:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aae1a848-90f9-3873-af46-a50a94d490f4 | -12.79141 | -54.00655 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc9627ad-52e2-3644-a7d1-15a4973c4916 | -11.82587 | -50.47003 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 60aef56f-2c3f-367d-b455-70c7ec1a1ad2 | -12.78312 | -53.99392 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c474770a-8f73-3667-b100-843cc209861c | -20.50061 | -49.62934 | 2026-09-30 04:55:00 | NOAA-20 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| afe9e867-7970-3e92-81cd-425b1aff5091 | -11.81901 | -50.46896 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8db019b2-848c-377d-a320-fc86bfe9597a | -13.53926 | -49.17077 | 2026-09-30 04:55:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ede8085-2080-31c3-aa9e-7aed1e665406 | -18.49251 | -45.14617 | 2026-09-30 04:55:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f94f0528-f314-366b-8811-69903eaf5c4e | -11.40203 | -50.98278 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ac973aa9-61e8-30bd-b5f9-0fd32ae1eaa7 | -12.78588 | -53.99813 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e19f8df-44d8-3a21-8a02-ea7eb4fd8bd8 | -13.3796 | -46.82512 | 2026-09-30 04:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 984b89f6-f56b-3afb-9b71-7857b7faea68 | -11.40425 | -50.96821 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| deff41df-d039-3c8c-906f-ded85f21cf08 | -18.23335 | -53.02314 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e534c2fb-278c-3e39-87e0-55e10ccb3eb7 | -11.36222 | -51.0286 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f088c1f8-f917-3f5e-9ba1-6badd6671e50 | -12.77954 | -54.01575 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c093f884-d054-3ffb-9139-65aee4ec05d0 | -12.78685 | -54.01325 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 548ceab0-3939-3798-82e6-1ffe245f2fc6 | -13.85694 | -46.37711 | 2026-09-30 04:55:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 885277cf-4ea5-33db-9cb5-2f3b13cf4508 | -18.89327 | -43.80561 | 2026-09-30 04:55:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 70ae3367-00f7-3ead-967f-c53b3c8fbf65 | -11.81672 | -50.46085 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5602d9af-18a6-352b-91b3-f91859bd635c | -11.39143 | -50.97366 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ba3e1630-7e59-304f-9944-e39749fd49aa | -12.30596 | -47.9603 | 2026-09-30 04:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6f3e12d1-3a37-3d58-9a83-125f8fb7c9c8 | -12.3442 | -48.19277 | 2026-09-30 04:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 44817040-2665-3b3e-b1e0-1cf9c4451287 | -12.31062 | -47.95557 | 2026-09-30 04:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fbff2b98-5468-3eca-a70f-4b00b95d4a10 | -18.3375 | -53.07451 | 2026-09-30 04:55:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6844d83-fd62-32de-a79a-d9cd7d8441b6 | -19.38604 | -44.70824 | 2026-09-30 04:55:00 | NOAA-20 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39f61558-d656-3e04-a3fc-56d07ee98249 | -12.07186 | -46.46305 | 2026-09-30 04:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fecce429-d1cf-3c8d-beac-31a297588957 | -12.30202 | -47.9599 | 2026-09-30 04:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a3990b25-bf9b-320c-ac44-d368ebebda09 | -12.34538 | -48.19505 | 2026-09-30 04:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 50de2919-c168-3227-a597-8cd3959da9f1 | -13.07171 | -43.27715 | 2026-09-30 04:55:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e7b39b88-4faa-383b-ac10-494693b252a0 | -12.78073 | -54.00846 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01d341a2-96c3-3810-9e8e-68ae7889b346 | -13.32549 | -43.93836 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8b48c9a-c3ec-362a-b0bb-9196c5cbf62b | -11.29375 | -50.98061 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85a290a0-25cb-31da-963a-d1dc0eefdd94 | -11.82244 | -50.46949 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2a66c4f1-0b4d-3b26-ab2f-1b2a84fb0923 | -11.7965 | -50.43571 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a44ae12-62dd-33f0-a662-5e161edda5d7 | -12.78133 | -54.00482 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 900b2373-dede-35c9-aa5c-7e5c0de7fba4 | -11.33644 | -51.03939 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a978c575-c625-3604-b14a-f06e73684a1f | -11.51766 | -48.32409 | 2026-09-30 04:55:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f930581-a9aa-3df3-8066-40bfa4b5305a | -11.39086 | -50.97729 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a3746f9-4655-3d84-b8f9-7f219dd17a37 | -11.85296 | -50.96251 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3d208512-7a63-3828-9581-ec01b2396b75 | -11.36559 | -51.02913 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3fa5d73-0225-3281-bdce-909fafc3da55 | -11.84 | -50.95672 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6e46d19c-9f2d-3db9-88a6-3dba78e1163f | -18.50318 | -45.14384 | 2026-09-30 04:55:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ec1555f-a462-35d8-9192-4ad59e9a3d66 | -11.84847 | -50.96932 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 967c26bd-5bab-3cb8-85b3-862498de0ff2 | -18.25578 | -53.04944 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d7e68e3-d188-329e-95c5-329c30a5ea97 | -20.5092 | -49.62509 | 2026-09-30 04:55:00 | NOAA-20 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d8a529b-607e-3a19-b601-cb99b7a4d6f5 | -11.80012 | -50.45438 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aebd63f3-e3c0-3531-b1fa-fbd32fb29740 | -12.31132 | -47.95052 | 2026-09-30 04:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 82b354eb-0e8e-39fa-9aa4-f0ecbba6851d | -11.40429 | -50.9906 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b97691e7-9677-3931-834c-4bf413c37ccc | -9.77943 | -59.01902 | 2026-09-30 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6d9577a-aeef-32f9-b5a8-8e4f6de3ab05 | -12.7926 | -53.99928 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f77061f-7f4c-394f-abad-f6fe7c226fb4 | -18.27524 | -53.05648 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1860e627-be77-3688-9919-eb9a0cb4362d | -18.88298 | -43.81794 | 2026-09-30 04:55:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README54.md)
