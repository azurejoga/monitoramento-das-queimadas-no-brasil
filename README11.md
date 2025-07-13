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
| 06596e57-6805-3249-a91f-27363849e6ab | -4.85978 | -43.2205 | 2025-07-13 04:46:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 815e40ca-ec03-34b0-b716-b025a04a28fb | -6.78251 | -43.96484 | 2025-07-13 04:46:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3857a9b6-b2aa-3212-a4f6-049910cb128d | -13.83921 | -45.89721 | 2025-07-13 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 100a0c23-b499-38f0-92a7-c7cb9f76b058 | -12.14779 | -50.23746 | 2025-07-13 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0785d79f-9ae5-3d34-b0f0-d9269eb133aa | -9.34051 | -58.83984 | 2025-07-13 04:49:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75bca056-bb4f-371d-90fa-ad23ad250dec | -13.14032 | -47.28549 | 2025-07-13 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 336b0655-20f1-3e90-b303-23dae7ce2d3b | -13.88116 | -44.45564 | 2025-07-13 04:49:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfaeab55-657d-3438-9683-d2fb14b69af6 | -10.67353 | -56.54701 | 2025-07-13 04:49:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c337e2b7-25bf-3909-b7ba-e6f9d0c27e7d | -12.44646 | -50.46848 | 2025-07-13 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9881a700-d8c9-390a-b183-f70dab9b45d1 | -11.93245 | -45.76522 | 2025-07-13 04:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28eff2d6-25b7-3f25-8ff5-c4ccdb3ff203 | -8.88789 | -48.08202 | 2025-07-13 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6d62141-5f03-3a1a-82e7-86591c4b0908 | -12.71018 | -44.40209 | 2025-07-13 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fd8c557-e134-3e3e-b43c-dcd00d5ea3ff | -13.10568 | -47.29502 | 2025-07-13 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ebef652-0b3c-36ce-b671-a9e4a096d60b | -6.63177 | -56.28426 | 2025-07-13 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c20b8fb7-691b-30b2-a1d9-ed743945d9bb | -13.83984 | -45.89248 | 2025-07-13 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f731c60f-6c59-3846-a1bf-7b02c73d98eb | -12.44703 | -50.46469 | 2025-07-13 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c3613be-4fe7-3150-8ff2-b499cfcbff28 | -8.34869 | -45.63783 | 2025-07-13 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1d3a32c-852f-3ee6-8745-b4182e064502 | -8.92757 | -47.34167 | 2025-07-13 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d0822a5-6665-3600-ba84-65789ebcbbf8 | -8.35296 | -45.6384 | 2025-07-13 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3aff6800-945d-38aa-a305-3bb9c76f6772 | -13.0273 | -47.81813 | 2025-07-13 04:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e9be9fc9-7731-36ae-a39f-2650c04be0be | -12.99984 | -46.26342 | 2025-07-13 04:49:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4db44508-c06d-3d34-b97f-3a487a9503b6 | -10.89987 | -49.20722 | 2025-07-13 04:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53d142b9-22a9-3c3e-9307-edf3220ebdef | -9.24221 | -64.40441 | 2025-07-13 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14fa3048-dc21-346c-b89a-8eb840d0558e | -6.62851 | -56.28423 | 2025-07-13 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e22ee3d2-012a-3c20-9d42-1b3277e3322b | -13.10833 | -47.3064 | 2025-07-13 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a74fbe8f-8583-3dea-bfff-f425cef93b78 | -12.11731 | -58.01356 | 2025-07-13 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7eccb627-15d9-3579-bdc6-818ae55a9709 | -6.62767 | -56.28363 | 2025-07-13 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 52096df2-1caa-333b-84d5-bf269119bef4 | -10.34513 | -49.91944 | 2025-07-13 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a12ab10d-fb45-36e2-b4b2-46431096b897 | -8.04398 | -50.11097 | 2025-07-13 04:49:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 26bca0b5-ac1b-318d-a6e7-4f194eb367a7 | -8.92303 | -47.34588 | 2025-07-13 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 653eb948-04a3-3203-bb29-933f3fbc6f5d | -12.42056 | -50.4615 | 2025-07-13 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d3a1f7dd-1109-338a-8140-f4d02678b66c | -8.88724 | -48.0864 | 2025-07-13 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| baa89013-24e5-34ae-aae5-76ac5570fd3b | -10.95411 | -54.37615 | 2025-07-13 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8e032fb-90e7-3368-a52d-16907f92a33b | -9.34139 | -58.83498 | 2025-07-13 04:49:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db17528f-6bc8-36dd-9093-65f8d3db9cd4 | -8.50885 | -43.28344 | 2025-07-13 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| eb5fac60-0a65-328a-853c-bae513e05f17 | -12.61088 | -48.3702 | 2025-07-13 04:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65d50101-76b9-3588-928e-dd1460d17415 | -9.2411 | -64.41017 | 2025-07-13 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7feed07-a664-3ad6-b446-f3556dce2382 | -13.11431 | -47.29285 | 2025-07-13 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| edeaac45-af06-3e72-9b51-4ca24d390ad0 | -13.84907 | -46.89365 | 2025-07-13 04:49:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 046304b0-481c-324a-8539-99a9e463c201 | -12.71216 | -45.02568 | 2025-07-13 04:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61ea1104-6e0b-32ef-9e00-af510b14eff3 | -13.10647 | -47.29865 | 2025-07-13 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b578d24-8911-3839-8e7a-3dd9005c6e7e | -11.73163 | -48.51669 | 2025-07-13 04:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 121fbfae-b755-3bad-b28b-c120f66fd15b | -13.02849 | -47.82132 | 2025-07-13 04:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35090357-5cd8-3aac-969b-986511f736c7 | -11.73097 | -48.52116 | 2025-07-13 04:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba4b8eaa-f5f2-3a2e-b164-02bc3601f44a | -13.13924 | -47.32414 | 2025-07-13 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0963d20c-95f8-312f-99fd-477540e11eb6 | -13.11024 | -47.29214 | 2025-07-13 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6afdd3dc-81cd-3b3e-8faf-f882409c4757 | -13.10696 | -47.29519 | 2025-07-13 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df9c7f77-5577-36e9-92d5-80b034161dc0 | -12.14592 | -50.24096 | 2025-07-13 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8382ac07-b67c-35bf-9c7f-98ffd48becf9 | -12.42114 | -50.45771 | 2025-07-13 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 99bd2132-c61a-3fbe-9774-011ffd9fdd34 | -9.91695 | -59.90881 | 2025-07-13 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb8f54cd-1c83-35f9-852f-d1d912835d55 | -13.11896 | -47.28918 | 2025-07-13 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd7e4e74-a5e3-31e3-946f-dd1989ea230e | -11.82452 | -47.51065 | 2025-07-13 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ff73f02-6000-3d3e-87d3-9d934f196404 | -12.14937 | -50.2415 | 2025-07-13 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92d40a45-99a9-3b0e-9a78-767c6d5269da | -10.50275 | -46.47334 | 2025-07-13 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a05ca49-f20f-33dc-99a0-24439e87472d | -10.12923 | -57.77684 | 2025-07-13 04:49:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40bcec95-db87-37ce-af2f-0e84b97d21e2 | -9.7973 | -48.56804 | 2025-07-13 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bac1fc40-48c6-358f-9580-4fb922107694 | -13.0289 | -46.27953 | 2025-07-13 04:49:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0235a2f-9c19-39fb-8e1a-59c264e701a1 | -9.92188 | -59.90977 | 2025-07-13 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4697c65b-add5-379f-9e29-bc0762616619 | -11.41601 | -46.42471 | 2025-07-13 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 438b2bbb-7bb9-3006-92f8-400c53a15264 | -10.08955 | -52.73902 | 2025-07-13 04:49:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae8ddc46-96dd-3da4-9b9c-e085d2ab2b69 | -10.8983 | -49.20625 | 2025-07-13 04:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67341503-9ac1-3e9b-8a6d-e21eccdf4c0a | -13.85277 | -46.89837 | 2025-07-13 04:49:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0747728b-e3ff-3e94-8c56-2e0f85d92435 | -8.34987 | -45.62959 | 2025-07-13 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ed4a21b-1495-39a1-ba53-180bc0f8b8c0 | -13.12358 | -47.28587 | 2025-07-13 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a949117-a517-3569-be6f-2e3e40c59400 | -10.7996 | -49.63249 | 2025-07-13 04:49:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f58005d3-227e-3e6f-91e6-d74f9737561b | -13.19385 | -47.26055 | 2025-07-13 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a82c2c08-232c-356a-8858-0a28d5871ef8 | -8.04505 | -50.10403 | 2025-07-13 04:49:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c7b3ea4e-220d-380f-94df-8e2f9426c97e | -10.57304 | -49.1284 | 2025-07-13 04:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a992088c-3d81-3131-b8ea-1ba391979764 | -10.1335 | -57.77758 | 2025-07-13 04:49:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90c8d457-d84a-30b1-8c38-fef691e1799f | -13.10522 | -47.29845 | 2025-07-13 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ad26570-b117-301d-a023-5ac3b21e0d8d | -13.13971 | -47.32062 | 2025-07-13 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85d20afd-6efc-347a-b1ea-e9df11c425dc | -11.9369 | -45.76583 | 2025-07-13 04:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 157c3838-3840-357b-b90a-77adf681fd45 | -10.89631 | -49.20663 | 2025-07-13 04:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f51059d1-8011-3d38-b261-ad3964c87009 | -9.24622 | -64.40383 | 2025-07-13 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 47a6162d-739c-3cdc-a796-df3f330c51a5 | -6.62705 | -56.28725 | 2025-07-13 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7274f99-3772-346b-9b91-062fa223a705 | -11.72725 | -48.52061 | 2025-07-13 04:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4e07530-3403-3cb4-a901-94b1c0ffe58e | -8.04841 | -50.1046 | 2025-07-13 04:49:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b89625e4-2781-3ee5-ada4-82d88c72556d | -10.50749 | -53.58977 | 2025-07-13 04:49:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 04694843-f3d4-3939-a22a-bfd1a3542713 | -13.02065 | -47.81971 | 2025-07-13 04:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 896897db-77ab-310f-b6cc-78e46781b75b | -11.72382 | -57.43897 | 2025-07-13 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4673681d-7b3c-371e-8891-e41837a5f337 | -9.02521 | -61.23142 | 2025-07-13 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58236914-d44e-3a1d-8ac1-a61a3882f184 | -9.02041 | -61.22684 | 2025-07-13 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7623c705-c6f9-3ba4-b08b-3be052b677d0 | -12.44472 | -50.45657 | 2025-07-13 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9754ee9d-b4aa-3498-a959-a15a0a79133b | -12.70524 | -44.40141 | 2025-07-13 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 042e38fc-962b-3cad-991d-fd645e872c9a | -10.57069 | -49.11974 | 2025-07-13 04:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 50df740a-242e-3dcf-bb35-bc8d76024edf | -10.59424 | -49.46661 | 2025-07-13 04:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f60555b6-8b94-3f52-a551-32c17ace0a92 | -10.34168 | -49.91891 | 2025-07-13 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a57dd84-e1e0-3bd9-b577-6789e135c95a | -8.01085 | -50.10205 | 2025-07-13 04:49:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 373c889b-cc72-30bc-897a-118890fb9eb5 | -10.84838 | -49.11184 | 2025-07-13 04:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b17298cf-e90f-3975-86f8-1bf563e92085 | -7.6105 | -49.93736 | 2025-07-13 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93c16a51-e25e-3d80-be09-7521acb3b2dc | -11.65628 | -48.2701 | 2025-07-13 04:49:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3cdd1c2-e829-3bce-bbf1-ac67c399ac8f | -13.83612 | -45.8938 | 2025-07-13 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bcc58903-0328-3697-b30e-a396b7859f49 | -13.02662 | -47.82319 | 2025-07-13 04:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9884d0c-ed1b-3d4a-ae24-cc5350ecdc04 | -8.00748 | -50.10149 | 2025-07-13 04:49:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b49f15c1-baea-3f5c-ac1b-e53ce455c679 | -8.92372 | -47.34108 | 2025-07-13 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b64a7e4c-ff34-3eb3-af19-c259c4705a2b | -9.24507 | -64.4096 | 2025-07-13 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7224e42a-ddfb-3dad-a837-1f60b67afdc7 | -12.42457 | -50.45824 | 2025-07-13 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fe64b433-5afb-384d-aa60-8b41b34a3b39 | -9.87379 | -45.34718 | 2025-07-13 04:49:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ccfd9b46-614c-3fb1-8e10-68c917281f98 | -13.02596 | -47.82801 | 2025-07-13 04:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a29ccde-be0f-35f5-982b-caf78dd4cbe3 | -10.05809 | -59.10937 | 2025-07-13 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README12.md)
