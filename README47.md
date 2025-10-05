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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a57e933e-8149-3d67-8d21-c648c4f2edc2 | -10.62714 | -43.31793 | 2025-10-05 03:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 934547dd-88fd-38dc-9857-8ef2a276f77c | -5.78147 | -42.93737 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| e6c06f2e-b14b-3fc7-a8e0-784ee6f4cbcb | -9.28587 | -46.01709 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 1b0a2101-b0dd-3563-bdbb-9496104bbcc7 | -9.57218 | -46.12798 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0fd3c1ef-a4dc-39d3-aae6-00ecb2956f23 | -6.23608 | -44.25328 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 89e9106d-cac3-3925-a0c2-0e4a0b619ab8 | -7.61024 | -45.47158 | 2025-10-05 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f82391af-d14d-3788-8ac6-950c2bcc00d6 | -6.71152 | -42.8358 | 2025-10-05 03:53:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 006eda49-5915-392a-abbc-59587ad0712f | -7.24798 | -44.88974 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b60088b-2daf-34fa-beeb-5d30e22744eb | -5.8288 | -42.46502 | 2025-10-05 03:53:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2133182d-dfc3-39e9-ae77-f13beaf3da03 | -8.58973 | -46.30231 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 5a2fcca6-cc59-3cdb-bc8f-81adccf5e45e | -5.78206 | -42.93388 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 1ca9a603-9ac2-3e2c-8e62-4855f6f27df6 | -10.68177 | -44.14253 | 2025-10-05 03:53:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c27c09bc-65bd-3211-aca6-ef4a518cc02b | -5.72016 | -43.84102 | 2025-10-05 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c460430a-58fe-3938-9beb-eabb923bc690 | -7.45909 | -47.18398 | 2025-10-05 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fbd88d5a-9b87-3652-87fc-581c2a13394e | -6.61696 | -38.10017 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO | PARAÍBA | Brasil | 2513984 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cc9db684-8cf1-33be-98f4-8b397945806d | -8.63327 | -44.89851 | 2025-10-05 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0af875cb-6d15-3ed0-b668-afd4611626d6 | -5.181 | -46.21424 | 2025-10-05 03:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6de33be4-3fcf-3879-be77-bae8c73c83f1 | -7.47604 | -43.02766 | 2025-10-05 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fd8bf57b-1739-3200-aa6a-85622422298b | -6.00452 | -42.51578 | 2025-10-05 03:53:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c4ec5329-fed6-350e-ae5a-45ddf5193271 | -6.33672 | -41.63034 | 2025-10-05 03:53:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 545f5744-f679-34d4-9c56-b95b46dde2e2 | -5.80275 | -45.7579 | 2025-10-05 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d4d9a094-8204-3832-a7cb-509e8fabbced | -6.15569 | -44.67316 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 6fe10917-0349-3136-b04a-4ac210b478ac | -8.55154 | -46.26871 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8f64e167-d1d0-31fc-91c8-5888ed5f9782 | -10.34608 | -48.15793 | 2025-10-05 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ccc7590-e504-36cb-aa45-3b68bd8cbf33 | -7.68497 | -39.61353 | 2025-10-05 03:53:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 173ee823-59e5-3bec-9bf3-bb9a2080c75c | -8.55649 | -46.32305 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ae5d09a-11a1-3a23-a61c-9701a0bfa673 | -8.85998 | -46.80517 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81396b37-10c3-37f7-8ad3-e1a0f5c10b7d | -6.72094 | -42.16786 | 2025-10-05 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5db92e3e-6229-3bcf-9b62-8ebc581bd778 | -6.42982 | -44.46867 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de7b969d-b079-32bb-bec4-79a4730e998d | -6.87587 | -44.50027 | 2025-10-05 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 211fce35-8793-3f6a-b2ed-4ce11a2d1336 | -9.90941 | -45.95641 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 8aa653ac-f34b-3a6a-9941-c8340e14d963 | -6.69852 | -43.88118 | 2025-10-05 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d647380f-6d9b-30b5-b925-0804125e5a52 | -6.59925 | -44.3178 | 2025-10-05 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf4bee6b-d56d-3118-9ed4-69a8559bcc9b | -8.86211 | -46.85938 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f9827074-fb59-3318-b3ba-20af98ca3ab7 | -8.27274 | -43.83577 | 2025-10-05 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cb1fa98c-e2ee-3f89-be0b-31ff2bf744dd | -6.69824 | -42.84327 | 2025-10-05 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| febb9522-9ae0-3349-84c8-ecbe2340795c | -5.87251 | -42.53671 | 2025-10-05 03:53:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 863b3d1a-3c79-330b-b0ff-453a7619175e | -5.97186 | -44.12849 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d63f5655-9932-35c7-b0b3-4e92b1ed4c60 | -5.26192 | -45.35652 | 2025-10-05 03:53:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 599bcac7-0fed-387f-aa13-820b732c280c | -5.47023 | -42.8027 | 2025-10-05 03:53:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2d7adf5e-02ec-363b-bd5c-7d6e8317572a | -5.79341 | -45.78384 | 2025-10-05 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d05e4da-468a-3016-b45d-d1e3793b2933 | -5.83511 | -42.45122 | 2025-10-05 03:53:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| df709774-7d25-3741-ad19-1e1194b8979b | -7.45853 | -47.1871 | 2025-10-05 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2cfcc151-962a-3198-9188-ae52fa2358a6 | -8.53371 | -46.31249 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 33093809-8fb8-3242-9d38-a1d48807baf3 | -5.90968 | -42.89386 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| bb53bf79-602e-398a-aa7f-a8787712d4ae | -5.88555 | -42.91614 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| dfddc84b-e3e3-33ee-9304-7f0a3af3ecc9 | -7.16279 | -43.26379 | 2025-10-05 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4e10ff62-c1cc-3520-b89a-380f113bb5ef | -8.90255 | -46.5928 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e5e6bd0-1aab-3a46-9a4e-925da8fcdc50 | -6.38064 | -43.88692 | 2025-10-05 03:53:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d16bb8da-2f2b-39d3-a7a8-ddbb242d952f | -5.99132 | -44.36567 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 602d335e-13c6-35da-b201-fc0a1fa4dd96 | -9.78525 | -46.77317 | 2025-10-05 03:53:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f51c220-e5cb-34dd-89ed-beadc2834eba | -4.56461 | -48.6116 | 2025-10-05 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a5eedfa-c8b4-3b48-bacb-027559f68ccc | -5.98189 | -44.36829 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2ffcc28-9a5a-3750-a581-b9e22902b177 | -6.69319 | -41.94247 | 2025-10-05 03:53:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 69bc02f4-572c-31cd-9915-558f4bc63f9d | -6.72545 | -42.16385 | 2025-10-05 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9b154ae4-8028-3953-91e1-6ee59a3d995d | -5.77954 | -45.74866 | 2025-10-05 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc9d8583-cba8-38c9-9e8c-8dd90aa12169 | -6.14683 | -44.67145 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| ec44f211-10bd-3c05-9c05-cc5446317247 | -5.25726 | -42.97485 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1fc4c399-b978-3832-b405-dc4cc337cceb | -6.00371 | -42.52068 | 2025-10-05 03:53:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2131b115-fd42-38c8-bbbb-34bcdb3e5a5d | -5.84022 | -42.85398 | 2025-10-05 03:53:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1dd241b0-4d06-3c37-a298-04eb32ecc321 | -6.45957 | -44.58689 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 49241304-a752-379e-8669-a2538d7c7b74 | -5.38044 | -45.69985 | 2025-10-05 03:53:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bebcc8a-1a7e-3859-af56-f13ec181ad6d | -7.71566 | -42.55827 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c1659fa3-f736-36c8-b9ae-9bf94ffaee06 | -6.33235 | -43.45812 | 2025-10-05 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1825bca-7dff-320b-8fd9-83bd042abb10 | -7.34832 | -45.21785 | 2025-10-05 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5169cf67-67c0-3b40-afef-e0e42213f9ad | -6.613 | -43.72246 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8b2b12c-9666-3e41-979f-31cc38e557d2 | -7.75416 | -42.60794 | 2025-10-05 03:53:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 520db153-db19-3813-906a-a5b28329c36f | -6.71499 | -42.7907 | 2025-10-05 03:53:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e092dfa1-3b76-3b07-bbe3-e8c687b12cdb | -5.84776 | -42.80822 | 2025-10-05 03:53:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 89e50288-6123-33bd-9454-c3a0032f43cf | -7.78725 | -44.51594 | 2025-10-05 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be6f68f5-527a-3bb1-880e-85fa8c100355 | -6.9222 | -37.43122 | 2025-10-05 03:53:00 | NOAA-20 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e8296392-801a-3871-a764-6985a205c7a6 | -6.91378 | -45.06368 | 2025-10-05 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 334d13c4-b65d-3e80-a5cf-bc3702a5502d | -10.64138 | -46.34628 | 2025-10-05 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 387e1a57-2955-3fca-82cb-45b0b582a5bc | -8.58496 | -46.3015 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| a7ef1544-c05f-33f6-94db-44f9eb48987e | -6.02301 | -44.02361 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e95cc3a1-cb09-3406-ba56-4b5fa3dbe3d6 | -5.81944 | -42.44139 | 2025-10-05 03:53:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6e9024f3-2aeb-3992-a2fc-df0bb1b5a5fb | -6.61713 | -43.72319 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0959be9-469b-34ad-8094-6aa2500cd176 | -8.23721 | -46.80682 | 2025-10-05 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 906be782-068d-35e7-953b-18c7d47d386e | -7.42381 | -46.50763 | 2025-10-05 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00c5ace3-47ce-3bc8-a58c-48ff763a140b | -7.0378 | -42.76124 | 2025-10-05 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4e13f566-5d0b-346f-b3d9-cf14c00901fe | -6.15578 | -44.64589 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 923dba27-e546-3d57-862f-19cf87fd2679 | -8.1863 | -44.14282 | 2025-10-05 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2e05b851-aaa9-332b-9def-f962aeb27005 | -8.84176 | -44.79445 | 2025-10-05 03:53:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77ed2e29-6a0d-3317-a4a3-3ede2291e7ac | -6.35497 | -41.6336 | 2025-10-05 03:53:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4eb5a71e-3977-358e-8c06-44affd68876a | -6.33174 | -43.46169 | 2025-10-05 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47235fe5-6a56-367d-b585-8e9e63ba8408 | -9.26205 | -40.49659 | 2025-10-05 03:53:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8aaebce1-9821-39a7-b220-15235f62fc25 | -5.85423 | -42.79354 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 614aac50-13dd-3bcd-86a0-f3fff472e4ad | -7.15525 | -46.09044 | 2025-10-05 03:53:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c48e6b41-410f-31be-a6fa-062320398fe0 | -7.46343 | -43.05476 | 2025-10-05 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 891cc90a-5549-399f-be06-f1e864732e2a | -8.57846 | -46.33797 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c103953d-77b1-3ec2-94d7-ffb713363f89 | -7.25388 | -44.88179 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db368f7c-4744-38df-abfb-bc43484a622b | -5.96477 | -43.51538 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f2f0d326-e48f-38d9-af40-e419bfe27e14 | -7.20253 | -46.86282 | 2025-10-05 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 285b2fae-a09f-3572-9cca-2a76b152fd8f | -6.01082 | -38.41138 | 2025-10-05 03:53:00 | NOAA-20 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 73f7b521-c2be-309a-bc53-ed654c59201d | -8.5449 | -46.27826 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 61174730-76e3-3316-b7d2-6081f0ce66a3 | -6.40812 | -43.06059 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 17a6db7e-ba20-36fe-a531-9fd74ba5fe8b | -5.95115 | -43.52084 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 524b50c5-5339-31d5-8b82-bd3583256d41 | -8.55741 | -46.31791 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dc74032a-89fb-3d6b-9187-931b1554758c | -7.01013 | -47.21912 | 2025-10-05 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54eb56ad-895f-3058-8e25-2a8f2f583a52 | -5.45954 | -43.40925 | 2025-10-05 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README48.md)
