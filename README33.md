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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6abeff8f-c4d9-3efb-8987-57f038ad5ac4 | -9.46183 | -48.30007 | 2025-09-02 04:14:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66a8b28b-374a-33a5-8f82-71a4080e0009 | -6.97568 | -44.34135 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e54932e-7fbd-3872-a6ca-bc1d3997f6ed | -11.64778 | -52.18106 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 4b97291d-3146-3f6d-8522-36ebbda15489 | -6.8196 | -52.82945 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2a2e6515-f82f-39d1-9a68-fd0cfd67f7de | -7.63389 | -46.55764 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7cc70d66-8e58-3ea5-aa0f-8c80c75aeb6e | -13.70317 | -46.93194 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f25e20aa-0935-34dc-9c9d-dad6407e0144 | -13.31647 | -46.83144 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e60de4b2-5f81-3bc5-ad9c-7eb37fb12a7e | -13.69288 | -46.93582 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 27abea16-abef-3625-9040-cd18e6813fa0 | -12.61515 | -48.18592 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 43ac12cc-e3fe-378c-82fa-3b033cc78a01 | -12.56167 | -48.25486 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ddab0e49-f4be-3b58-a47f-c28b952b2b1c | -11.81625 | -51.54113 | 2025-09-02 04:14:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 59d4d271-19f3-3cae-ac32-94b79eeccfde | -10.05802 | -48.13155 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cff2718f-ab61-31fe-b8e3-6019fe3136e9 | -11.01725 | -46.93928 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2aec880b-56f3-38c2-b81b-2f2ce2fb1a7b | -8.12487 | -44.99908 | 2025-09-02 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56429f63-cd62-335f-9616-f5c489e056e1 | -9.49755 | -48.86367 | 2025-09-02 04:14:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| edd2e7f8-057e-3dbd-a131-e12144f658ec | -12.86375 | -48.17513 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 026fde70-0d51-3047-86f1-b294762eec66 | -11.67518 | -52.18775 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 0cb0ba1a-cf01-3916-ac5a-aa7f48f080cb | -11.10264 | -44.62422 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 87a073f7-6d3e-3ed9-b1cc-8aedba59b25c | -12.59219 | -48.20957 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7798e3f8-08c1-37e8-aa4b-e5a293aa1e6e | -11.64962 | -52.19814 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 4be757fd-bb01-3c7a-a7c8-860f38996765 | -9.64202 | -47.79336 | 2025-09-02 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| caecb44e-b8c0-3b43-b50e-e821ea8c12e3 | -11.54924 | -44.84896 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fe0a749-8a34-34c6-9b6a-7a2475bda230 | -6.97187 | -44.30095 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63e43f5c-3347-3c81-a388-72914cb20d50 | -11.09653 | -44.64126 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 01ff3d7c-195a-342c-8300-820cac34cd4b | -11.28323 | -43.64946 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5aa47a68-0770-33b3-9c25-cf514c8e84e2 | -6.80512 | -52.81546 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4134a2f9-0fad-38e8-a0b1-38b688bcc5a1 | -11.75658 | -47.82723 | 2025-09-02 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ea440aa-ffee-37b4-a31a-fdee8d6bb3f4 | -9.7388 | -48.96495 | 2025-09-02 04:14:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a497f8a9-035a-3ae2-aab0-df05850ff6aa | -10.47332 | -51.62599 | 2025-09-02 04:14:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 23b8e6ff-cfc3-3101-a1cc-7b8bb15fa85e | -12.17497 | -50.13213 | 2025-09-02 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88e4678e-39c4-3e5d-a117-71d8b880bd8b | -12.61872 | -48.17978 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 4591a30b-f788-3d17-9c3f-767091bf83bd | -12.78695 | -48.07703 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8e95d5c-bcaa-3e9c-9afb-3d047421b9ff | -6.91488 | -45.56628 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45501ba3-557c-37f6-af94-90dddb4d1f52 | -9.92193 | -51.62165 | 2025-09-02 04:14:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| df34eec8-1436-366f-b6b7-6db36d7d6afe | -8.70631 | -50.44786 | 2025-09-02 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e0c93e5-48a0-32bf-a821-f0b698950482 | -8.87291 | -45.75562 | 2025-09-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba98e013-b3be-32bf-b55b-9389118b3f03 | -7.99503 | -44.04365 | 2025-09-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90da81cb-b10f-3436-9fbe-4ddbe39b5365 | -11.37703 | -43.61405 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d10b35de-e236-32f1-bf76-72f818faf414 | -7.46908 | -44.80515 | 2025-09-02 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bbae7e2-6318-3700-8309-e33d9ddd79af | -7.31527 | -44.27963 | 2025-09-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d615287c-71bd-3002-9318-5fa2978092a1 | -6.64368 | -44.10402 | 2025-09-02 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35bac8d5-bd75-3bc7-8793-60c78a5a010a | -6.58483 | -44.06588 | 2025-09-02 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9469eef4-d170-3ecd-a9b3-f6e2b1878427 | -8.83002 | -47.52072 | 2025-09-02 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18afa479-f1f6-3635-a6aa-c6649bb45bec | -11.67558 | -52.21992 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 14b293cc-46e7-38e2-9998-80b2ddb4ccb7 | -11.65726 | -52.21087 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 38986a1e-efb7-37b2-8287-6cc8930832df | -7.06079 | -45.98413 | 2025-09-02 04:14:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9f2ee37-c4dd-35e5-b31a-8e286da1ca0c | -12.62606 | -48.18117 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 876458db-a468-37cc-b922-4965411054a2 | -7.63056 | -42.64912 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dcc164f2-4a26-3a27-8525-20dbe58814c2 | -6.79928 | -52.81977 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 01c4aad9-056e-3a43-a834-add8032b84bb | -8.71984 | -50.45025 | 2025-09-02 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 697d5008-923b-3276-b21d-9d4e975037b6 | -12.57937 | -44.80028 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdae6297-b5f3-3a2a-bf4d-751adad70852 | -7.97627 | -46.45738 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 286e016c-7c1b-34d1-b3ed-b01b10469234 | -12.57993 | -44.79676 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82b5ba12-2fa1-375b-b7a2-b3abe6ba33e2 | -6.83459 | -52.8116 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72b6175b-8163-339c-9fd2-e7abb719ea6e | -9.83113 | -48.61176 | 2025-09-02 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4aa59f0-99cd-3f60-a148-5401284563b5 | -6.84972 | -52.82143 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8668a33e-a575-3efe-845a-5816572db617 | -7.06282 | -46.24112 | 2025-09-02 04:14:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbe040b9-5f4a-3297-8605-9ae5026e8802 | -6.81541 | -52.82112 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 687d37e2-4ae4-3a3e-9109-125f283e533a | -11.85503 | -46.7823 | 2025-09-02 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e8ef66e-701a-3865-a196-d5759b979a9e | -6.98529 | -46.1118 | 2025-09-02 04:14:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f5e9acd-3275-3c6c-9d12-1c16f5087005 | -13.53089 | -46.99993 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 763468e0-b686-37a8-8d3e-bea96fe5c213 | -10.05308 | -48.0919 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 89b28b66-e3c0-3166-8745-6a3d432da5e1 | -11.09322 | -44.64072 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 2728df88-48ad-345d-bf4c-3b664b15845a | -11.90343 | -46.67366 | 2025-09-02 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b1f4cf8-98f0-3ce5-a28a-00baf32ca10c | -7.16209 | -44.9231 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2797c1f8-9bc3-333f-aadb-5b2799c8bc38 | -8.87675 | -45.77552 | 2025-09-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b404f1a-e6f1-336e-bd38-6f6229de0b1d | -13.397 | -47.06548 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f1fb958-769e-372a-9d2f-a1cdfe5358fb | -13.28923 | -46.93098 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a422b42a-ad98-3d74-bf7c-18ade6c0037f | -11.95931 | -45.84578 | 2025-09-02 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 696de569-f174-3117-9e64-f4d81a9064ad | -7.12726 | -44.43869 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d3f8096-f06a-3177-8d9b-71f9815a6c7d | -6.799 | -52.81824 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b41cda90-e20e-3943-a966-7015cfe0c55c | -11.67075 | -52.21899 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 153694cb-1f3f-3b1a-9423-b6d8747ebc7c | -9.83514 | -48.60957 | 2025-09-02 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 439d5613-535d-351e-8695-85f43b97a75a | -6.89834 | -44.23133 | 2025-09-02 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77edf751-95ad-387d-999c-41d4fa159139 | -6.79074 | -44.62273 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d3cb153-a01a-3239-a353-ca6c1606fa45 | -6.81569 | -52.82257 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7b2406e-d5e7-3427-b679-f7002adecaa7 | -9.84245 | -44.68662 | 2025-09-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7adb874-aa06-3480-9279-2bfa88811330 | -13.58831 | -46.926 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2dc28032-d16e-3a77-bcb8-b12a2cf08c3d | -10.06592 | -48.8856 | 2025-09-02 04:14:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7157d578-ab37-357b-966f-83f4af6a6470 | -6.64208 | -43.9636 | 2025-09-02 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16963f61-f7fb-3de9-b529-ec07dcee6ed6 | -11.37923 | -43.5999 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9401bf5e-4c2f-3009-813d-0ce708febb3a | -8.86744 | -45.78945 | 2025-09-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0123327a-556c-345e-b9a7-7b10104fff09 | -13.56502 | -44.83892 | 2025-09-02 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6d540dd9-e86e-38d2-9caa-9faa4a751a74 | -7.06729 | -44.34181 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c830183-e7ba-3695-9966-b93d270623e7 | -11.64876 | -52.17569 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 128264d8-48bc-32b2-a2b1-d735031b19a6 | -7.69571 | -50.27456 | 2025-09-02 04:14:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 50251eeb-553c-39d8-9a82-aa34324ca63d | -8.31021 | -55.10246 | 2025-09-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c2d28c9-ac46-30f9-a17c-9117a54754d4 | -11.38535 | -43.62624 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6846cfa-5b79-33cb-8212-d6c9e2204cd2 | -12.93967 | -48.08344 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 92d440c6-d84b-3b74-b4e3-e07b51a19a46 | -11.09374 | -44.65883 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ce83d7c4-f27e-34b8-9ea4-ed0ba99b4a74 | -9.49815 | -48.86018 | 2025-09-02 04:14:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c92ddf7-2601-3196-a749-a6f89a3f1b85 | -8.136 | -49.82953 | 2025-09-02 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 267f3bf2-e8e3-3d93-9d2f-3ef43a965df7 | -11.87511 | -46.72519 | 2025-09-02 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80e9bd3c-5f1a-3e36-bff6-c6c82d8ecd81 | -13.30896 | -46.83409 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 50a49438-5c45-3626-937f-4cf90ab9e791 | -12.62159 | -48.18504 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6f9a6c34-2881-3cfb-9e22-88c370c8f067 | -7.88523 | -45.18132 | 2025-09-02 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 404e74ed-c773-3942-9838-8bc6b45012c6 | -7.57328 | -45.22577 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9add0e92-4dd5-3b3d-a421-c8f486d4e872 | -11.93218 | -50.61348 | 2025-09-02 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be64e85b-32b3-3c63-8100-3d0b47d1f794 | -8.33374 | -47.40009 | 2025-09-02 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 415413cc-3061-39fb-bbb9-705f35a3e33c | -13.34009 | -46.85967 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README34.md)
