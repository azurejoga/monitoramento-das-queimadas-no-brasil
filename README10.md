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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e22c3e35-6b61-3147-a3c4-71f85d2a06b9 | -19.47705 | -46.54893 | 2025-11-30 03:57:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c5f8f19-9917-3733-8955-b8684e520989 | -18.41355 | -46.84222 | 2025-11-30 03:57:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d970448c-dd4e-3fab-a810-4320ad8ea6d1 | -15.71439 | -50.00847 | 2025-11-30 03:57:00 | NOAA-21 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1b066cf-8c3c-3c88-8e30-d15c937971a7 | -17.86144 | -44.31673 | 2025-11-30 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c07e4ee7-62d3-3dd5-a932-3443c518c39c | -18.69301 | -46.812 | 2025-11-30 03:57:00 | NOAA-21 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7fbadb06-e7be-33f7-8077-51a474effdf5 | -16.21602 | -52.18003 | 2025-11-30 03:57:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e28fe5e-3c2c-32c7-b016-faa02200a427 | -18.61824 | -45.23144 | 2025-11-30 03:57:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5a6f6226-f380-3070-9a0f-eadd523bd6f8 | -19.97864 | -47.83894 | 2025-11-30 03:57:00 | NOAA-21 | DELTA | MINAS GERAIS | Brasil | 3121258 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b36c8db-7a84-33b6-b55d-3e4cf29f7cb7 | -20.59777 | -51.6102 | 2025-11-30 03:57:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e900dcac-21f5-3016-acd2-0f42bc468ede | -21.62384 | -44.84724 | 2025-11-30 03:57:00 | NOAA-21 | CRUZÍLIA | MINAS GERAIS | Brasil | 3120805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 78fedd0f-28d8-371e-9e38-9a780fedb704 | -17.84912 | -44.32346 | 2025-11-30 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c177286e-81d8-3efc-8abc-12bb68fe55e1 | -15.71508 | -50.00502 | 2025-11-30 03:57:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b9b08bb-549f-3f30-90b9-9396e0c099d1 | -16.22107 | -52.18581 | 2025-11-30 03:57:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cf8dd8d-27ae-3b9d-8828-1811a23c95ef | -18.93291 | -48.48779 | 2025-11-30 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a16625f3-8c97-3458-b883-d332abc28c1e | -18.14834 | -47.13284 | 2025-11-30 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7294192c-9ed5-3644-9b84-38693debea5b | -21.00192 | -49.30725 | 2025-11-30 03:57:00 | NOAA-21 | CEDRAL | SÃO PAULO | Brasil | 3511300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| baa31c9a-ea6e-33aa-81a1-d239c05cb84f | -18.15587 | -47.13922 | 2025-11-30 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c7431613-a6b3-3515-a20d-4a3a92536c77 | -20.18905 | -52.38333 | 2025-11-30 03:57:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 924e4d38-cc5c-3ef2-beb6-0db406538a7e | -15.32273 | -42.05296 | 2025-11-30 03:57:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 44344d31-5253-3aec-a5b2-c072dbb70064 | -17.97373 | -41.70732 | 2025-11-30 03:57:00 | NOAA-21 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8cac8266-c91e-394e-9b60-badea7bc12fd | -22.53801 | -42.11652 | 2025-11-30 03:57:00 | NOAA-21 | CASIMIRO DE ABREU | RIO DE JANEIRO | Brasil | 3301306 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 15a4c84b-ea86-3097-98e2-21c23a013bf3 | -17.38735 | -42.46817 | 2025-11-30 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 714b88f6-c4d7-3bb1-8f86-432ea989b70b | -18.13003 | -47.15983 | 2025-11-30 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 158a46ff-fb5e-38e6-a35d-782fda5eeab6 | -21.41863 | -46.64234 | 2025-11-30 03:57:00 | NOAA-21 | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bbb2ca60-017c-3cf4-b893-f5a3665d21a2 | -18.12244 | -47.15371 | 2025-11-30 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1af6ba8-0908-35dc-8a89-b5bb33731493 | -19.98289 | -47.83989 | 2025-11-30 03:57:00 | NOAA-21 | DELTA | MINAS GERAIS | Brasil | 3121258 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2ce8e7a1-0697-307b-b74a-dc8812f7bb5b | -17.85501 | -44.31087 | 2025-11-30 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc469889-af54-3f52-bdfd-8f9646bdeddb | -16.76534 | -51.35302 | 2025-11-30 03:57:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2c93fcec-7674-3c11-acca-35897c87d60a | -16.21727 | -52.18277 | 2025-11-30 03:57:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3aaeadd0-0040-365f-b9e9-ebdcf7a272a1 | -17.38397 | -42.46758 | 2025-11-30 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd15510b-794e-34c1-b42c-e50c7909ff02 | -17.3846 | -42.46379 | 2025-11-30 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00713a3a-9367-3d26-bbbc-d5a4bf64517a | -21.24649 | -44.71659 | 2025-11-30 03:57:00 | NOAA-21 | ITUTINGA | MINAS GERAIS | Brasil | 3134509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f4e05187-57d0-3e5d-ab20-e7be8521ef69 | -16.2233 | -52.18396 | 2025-11-30 03:57:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d97e4ec6-bf1b-3d4a-b7e9-b2519db8b48a | -17.72231 | -48.20297 | 2025-11-30 03:57:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d4b65e6d-a3d9-3d21-a254-c2ab6361f310 | -16.2223 | -52.1885 | 2025-11-30 03:57:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74f3cb9a-1306-3caa-a23b-3c331fcc86a9 | -18.93382 | -48.48309 | 2025-11-30 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bef3b0b5-0edf-35b6-a7ff-f327562dc531 | -17.8586 | -44.31159 | 2025-11-30 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e3fbed1-6201-3772-823f-9b12c311f899 | -20.17873 | -52.37646 | 2025-11-30 03:57:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eadb43a8-1f47-3434-90e4-6d1085f023ad | -21.15109 | -48.61503 | 2025-11-30 03:57:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7a6a7593-d1a6-3ed7-a0d4-18f8f95f9b8e | -15.32335 | -42.0492 | 2025-11-30 03:57:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4c4c8579-3589-3845-aa8d-9c60ec8892fb | -18.13583 | -47.15243 | 2025-11-30 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f89763f-d1f2-3e0c-823b-e4d23151d2d8 | -18.11905 | -47.14858 | 2025-11-30 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34d21f19-aecb-3e72-a717-85a5a6edc2bc | -22.29856 | -43.47453 | 2025-11-30 03:57:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 96a4c15e-45f5-36f9-bf4e-a994fc748ae5 | -21.00649 | -49.30832 | 2025-11-30 03:57:00 | NOAA-21 | CEDRAL | SÃO PAULO | Brasil | 3511300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 7b3cfe81-30f6-3900-a43a-ffbd8fca25dd | -20.18343 | -52.38198 | 2025-11-30 03:57:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| daac6136-186b-3524-94bf-bc7663073089 | -19.09343 | -48.59006 | 2025-11-30 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 30f4b0e4-a7e8-3ed9-898d-51274445b3c1 | -22.5386 | -42.1128 | 2025-11-30 03:57:00 | NOAA-21 | CASIMIRO DE ABREU | RIO DE JANEIRO | Brasil | 3301306 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cea77404-5703-3e83-9336-8654b5766163 | -23.18439 | -45.66226 | 2025-11-30 03:59:00 | NOAA-21 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 97f056e8-06a7-35c7-ba03-9d79b9407da7 | -22.12177 | -45.36985 | 2025-11-30 03:59:00 | NOAA-21 | CONCEIÇÃO DAS PEDRAS | MINAS GERAIS | Brasil | 3117207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a1fc5719-a582-3127-8a27-cb84d2a06f2a | -21.53729 | -49.52771 | 2025-11-30 03:59:00 | NOAA-21 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 85fa14f5-2de1-3f07-b10d-58ad7098cae9 | -21.20829 | -50.46611 | 2025-11-30 03:59:00 | NOAA-21 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 052db279-91ba-3221-8fdc-5be2e47e44ac | -22.94575 | -47.2868 | 2025-11-30 03:59:00 | NOAA-21 | MONTE MOR | SÃO PAULO | Brasil | 3531803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f105bccf-f690-33cd-8edb-2d6565d43147 | -22.98162 | -46.23981 | 2025-11-30 03:59:00 | NOAA-21 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b688a12a-0709-36eb-a02d-c292a73cb631 | -22.48828 | -47.4779 | 2025-11-30 03:59:00 | NOAA-21 | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4559c8d6-b626-3126-904b-da22c060db53 | -24.07341 | -51.0596 | 2025-11-30 03:59:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| e3c2f213-fab6-38fc-b6d2-73ccdd4e2eb8 | -22.34394 | -43.51452 | 2025-11-30 03:59:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 02b8822d-c32e-3128-91fc-c865e901cc59 | -22.71623 | -43.23727 | 2025-11-30 03:59:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 611a24b0-7461-3456-96c0-563095b63a6d | -22.49341 | -46.93464 | 2025-11-30 03:59:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3d69ca35-5768-3ae0-b6e7-d8ce056b7bd7 | -21.53269 | -49.52668 | 2025-11-30 03:59:00 | NOAA-21 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 38d5265c-05c0-344b-b1a2-ab8a1d9d934d | -22.67686 | -43.47785 | 2025-11-30 03:59:00 | NOAA-21 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6d94ce4c-28b5-323e-a235-815401cbaf14 | -22.60438 | -45.76954 | 2025-11-30 03:59:00 | NOAA-21 | PARAISÓPOLIS | MINAS GERAIS | Brasil | 3147303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a08d7b55-ccb8-3265-add4-ff709fa7994b | -23.18881 | -45.65826 | 2025-11-30 03:59:00 | NOAA-21 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| bd94da7d-1bbd-34e2-a76c-549b8d9068c3 | -25.23767 | -50.76263 | 2025-11-30 03:59:00 | NOAA-21 | GUAMIRANGA | PARANÁ | Brasil | 4108957 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 56eaab2e-97e5-3d45-8f62-826a149d186c | -22.12752 | -45.12843 | 2025-11-30 03:59:00 | NOAA-21 | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ba97d67f-a4de-318d-a7fc-8a9a85af5ab2 | -23.19617 | -45.11805 | 2025-11-30 03:59:00 | NOAA-21 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 566d5378-1ede-35e0-9434-e580dfc52134 | -22.79148 | -42.19205 | 2025-11-30 03:59:00 | NOAA-21 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 306fc47f-5959-3d59-a573-683bf7cbbc5d | -22.74006 | -46.59219 | 2025-11-30 03:59:00 | NOAA-21 | PINHALZINHO | SÃO PAULO | Brasil | 3538204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1a401a5e-cfd0-3be8-9a1e-20888c943668 | -23.54804 | -47.20724 | 2025-11-30 03:59:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| df6de8d5-bd45-3fd2-9c32-06e76d0d9282 | -23.1852 | -45.65765 | 2025-11-30 03:59:00 | NOAA-21 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c887a23d-6541-3555-979b-2200d759220d | -25.23659 | -50.76779 | 2025-11-30 03:59:00 | NOAA-21 | GUAMIRANGA | PARANÁ | Brasil | 4108957 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 398534c1-cbab-35cc-91ea-860375bf51ea | -22.97947 | -46.24175 | 2025-11-30 03:59:00 | NOAA-21 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| df49fe92-f84f-3450-b17b-2e9d9ef969f1 | -22.84627 | -47.21256 | 2025-11-30 03:59:00 | NOAA-21 | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 055f9c3c-df00-3d43-a539-14ce04bc1f4f | -22.47054 | -43.34388 | 2025-11-30 03:59:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 475c3939-1ca2-308e-bea2-34f5b6012665 | -8.163 | -43.229 | 2025-11-30 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| 137e6bd9-0c96-3a20-bed9-84b3f4c4852d | -8.1633 | -43.2055 | 2025-11-30 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 115.7 |
| b01ceb2d-0541-36ea-b3b4-35690d38eb7b | -19.8675 | -57.7808 | 2025-11-30 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.6 |
| 8fa4d9f2-63c6-3683-9cc0-a522a0d94960 | -8.1822 | -43.2034 | 2025-11-30 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.8 |
| 67d90b3f-9aab-3e21-826c-028b1eec1d8b | -19.8473 | -57.7835 | 2025-11-30 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.1 |
| 10d4bbca-5734-3119-969d-0c543d13c502 | -19.8675 | -57.7808 | 2025-11-30 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.9 |
| 9a4909fc-c49d-3cdf-9bf4-40f1cc0e2c66 | -8.1633 | -43.2055 | 2025-11-30 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 112.1 |
| d0b5fa01-7a49-3bfd-9fcd-a0175088f0b4 | -19.8675 | -57.7808 | 2025-11-30 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 135.5 |
| d35f9990-1dcf-3e46-8a0b-b59fbfc281fa | -8.1822 | -43.2034 | 2025-11-30 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.9 |
| 6c0e50a7-b87f-37ab-8933-61b23b56391f | -19.8473 | -57.7835 | 2025-11-30 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 9c30303c-0a99-3ce7-bf40-d04495f00832 | -8.1633 | -43.2055 | 2025-11-30 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| 8e77adbb-6afe-3be3-a26c-9348993d3957 | -12.0004 | -49.2683 | 2025-11-30 04:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 329b6d0a-59c1-31bd-9e98-97fd3f12d817 | -12.0195 | -49.2659 | 2025-11-30 04:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| ebe3bde4-fc7b-3f30-8558-94362be98385 | -3.44205 | -41.49979 | 2025-11-30 04:23:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fb4c2911-40b4-340d-8d65-8ec486391753 | 0.7682 | -50.80334 | 2025-11-30 04:23:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75ff8f12-a926-3081-92f9-eb1215456d83 | -2.89893 | -45.26764 | 2025-11-30 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4dfebed-88c8-33d8-89f1-1d6ce46c26d1 | 3.3505 | -51.31047 | 2025-11-30 04:23:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abcbf466-1449-3574-bf0e-42cfc4dd0f28 | -2.44574 | -47.0806 | 2025-11-30 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e0d0305-bc46-3c7c-ac0b-f53c31d71a6c | -8.16675 | -43.21518 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 1f9db97a-cb48-3523-b8e7-bf415ed2ed30 | -7.74795 | -44.18363 | 2025-11-30 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3cd91a4-6b31-318e-b73d-4dfcae50ebe7 | -5.7109 | -45.63019 | 2025-11-30 04:23:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7db89b0e-6347-30f9-9250-1ad67585e801 | -2.16525 | -48.4297 | 2025-11-30 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4e6284c-4399-3e13-9cb5-11c5b0e744c0 | -7.73792 | -44.18209 | 2025-11-30 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 628c201d-462e-34ee-bd45-950856d63b18 | -8.04413 | -43.13192 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4b4cd0e6-5630-3f8d-8912-76ef8cef2ae6 | -7.48052 | -41.78768 | 2025-11-30 04:23:00 | NPP-375D | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cbbd4fb7-962f-3e0e-85eb-e128bab5b3be | -8.04464 | -43.12363 | 2025-11-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| b40700b1-ecb2-3711-895b-5a79348850e3 | 0.76333 | -50.80411 | 2025-11-30 04:23:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README11.md)
