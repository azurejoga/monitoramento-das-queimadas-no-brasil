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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4c57315-82b2-3526-bb9a-b28edb44576a | -12.6328 | -48.16419 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74cf55fd-042a-354d-b091-e05364f8b0bb | -10.33613 | -48.14197 | 2025-09-02 04:14:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5fe6d72-c47e-3880-b62d-65a133ab2f93 | -11.02788 | -46.85395 | 2025-09-02 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb8e9925-04fb-3755-a0f5-3e13a3311bbc | -11.41817 | -55.18977 | 2025-09-02 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be3efbdd-9bee-3686-a4fb-506264710aff | -7.62735 | -44.00637 | 2025-09-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb29512d-2f17-3a33-89ee-81003deacf35 | -11.09929 | -44.64531 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 0192487b-9ee8-30fb-a17a-1e46ea60f735 | -13.50543 | -47.00341 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9dd4c072-8016-36cf-b01c-b00da0543324 | -12.61592 | -48.18134 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 8291379b-4a69-3c37-a9e8-c031fbf45528 | -6.96862 | -42.08378 | 2025-09-02 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 842ab98c-6045-378b-a3e3-5f7dc4f0233e | -6.88704 | -45.8489 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c5624884-7492-3f14-9d62-64226a137e2f | -9.64796 | -47.80378 | 2025-09-02 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd9e432f-7751-31f3-a21c-65050450938a | -6.88099 | -45.86402 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 64bfe3c4-0279-3890-ac37-d798affb7dbb | -8.87453 | -45.76742 | 2025-09-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59a944d8-2e4f-3489-be76-c10bb7e42048 | -10.28666 | -47.46986 | 2025-09-02 04:14:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 127ec000-0fcd-30de-84c2-1568835b8c9f | -12.80891 | -48.05856 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f07657a0-db62-3ed1-be8f-d43558071e27 | -14.05422 | -44.55597 | 2025-09-02 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 528c390b-4a9a-363f-8cf7-16dbd51bfcbb | -7.21847 | -44.05499 | 2025-09-02 04:14:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16b62d0b-5169-3f23-be43-3961f4e848dc | -9.12235 | -46.05275 | 2025-09-02 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3ff291f8-467b-3c57-a709-9e2577961a95 | -13.69778 | -46.8843 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99cb0aa5-19d4-30be-a15c-7251ef64df50 | -11.97041 | -45.86267 | 2025-09-02 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 896bdc2e-8239-3df1-af70-3dc15fb3396c | -13.59012 | -48.14074 | 2025-09-02 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ed0e50e-5fd3-328c-a215-875488f96c54 | -11.65698 | -57.369 | 2025-09-02 04:14:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 65e2e832-db08-39ea-a0fa-9b19b9aef175 | -8.81509 | -47.4884 | 2025-09-02 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66c2e822-cc72-3da8-beca-6f7cc2a75158 | -11.90407 | -44.88189 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93709294-8d03-3d6e-bd1a-0ad48934533b | -11.95477 | -45.78881 | 2025-09-02 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e2599607-ea27-312e-a154-c0f385b52379 | -11.67109 | -52.20928 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 012b62fa-01b8-30b4-ac23-0f23cc5afbb0 | -13.70061 | -46.88852 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51b58903-859f-33b5-ba2d-e663179d9f47 | -6.8543 | -52.7959 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9428088d-402c-3ad4-83f5-7a3f148bbcd4 | -10.75154 | -49.58038 | 2025-09-02 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc8aad99-06a0-3954-ac65-bf96f65f6747 | -12.57722 | -48.253 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2e25599-50dc-38dc-8a5a-ff1fdb387c77 | -7.78637 | -45.44676 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8929a682-29f3-3b3d-9fb6-b159897fa063 | -10.05982 | -48.09816 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fbf30b0-be58-3eb8-94ba-f842875d5909 | -10.05606 | -48.09731 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 261b067e-b011-3c1b-b2e6-59fd93984187 | -12.93444 | -48.09218 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4359cea8-0df0-330e-92a8-2f0bd4b2e838 | -6.03722 | -52.17934 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2e823bd-4e09-32e4-978b-702f29ac20e4 | -12.96674 | -48.10053 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99690862-e211-3b0a-a41b-de6aa6a32409 | -14.04202 | -44.61222 | 2025-09-02 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 83381024-2cb9-3515-8b76-3b3ff647f939 | -8.88541 | -47.97269 | 2025-09-02 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93000d8a-a3d0-3f3c-8726-22a83980cba0 | -11.54574 | -45.0624 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c88dde1d-5309-3580-a659-2d1d9c60b3cd | -11.85376 | -46.79006 | 2025-09-02 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aad704b8-e233-3d29-bff7-a0a50e4efc3a | -12.99146 | -48.10982 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bd1af5e-8526-3936-8cfd-c5fbc9af81ce | -11.10703 | -44.63936 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7125c542-b187-32f4-a6bd-1f39d6dc6ed2 | -7.87291 | -47.96323 | 2025-09-02 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5c4f115-65ed-39e8-a630-54bdab26f4bd | -12.87341 | -48.05367 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0bb12c23-e603-3768-804f-f0d1fc7c45e3 | -7.4961 | -45.35493 | 2025-09-02 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c1059ab-1f2a-35e6-870f-c0573f8242a1 | -13.32547 | -46.84111 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 511b8124-2d0c-3628-b027-d26e41391e54 | -12.80817 | -48.06292 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ab96c875-570a-34be-adb4-d908beb676fa | -12.86314 | -48.04793 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 454391e8-e53c-300d-a182-fff475a6877f | -11.67416 | -52.19309 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 25.4 |
| becd113c-4199-3375-b65b-9bba651484d4 | -11.3848 | -43.62978 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25cb0733-1e78-31cd-81a0-4b516642abda | -10.05201 | -48.12097 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fe1f8540-71bf-3c6f-b2a8-5a852f93e815 | -10.83641 | -45.03752 | 2025-09-02 04:14:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 634ef5d5-c144-33fa-b9f1-bbd51e8e2987 | -11.85908 | -46.7142 | 2025-09-02 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c0570647-4fca-3fd3-a69f-7e29a257f2dd | -12.78329 | -48.07641 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b0e913b-e0dc-3fe9-b3b5-e949b9bbdf97 | -6.64984 | -43.95768 | 2025-09-02 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14fc2327-cda0-3ce0-95cf-89257c7f8751 | -6.94606 | -44.35493 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2932a353-bd08-30cc-8c04-438722cacddf | -10.444 | -54.78062 | 2025-09-02 04:14:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1fb1129d-83f7-31d0-8d9d-e94845db2e4c | -10.97215 | -50.77377 | 2025-09-02 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb3c0d73-afbb-3a66-b578-da7c7b2a23c9 | -10.05144 | -48.10147 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85c7a7e4-aa53-38c6-b02f-15b40213c907 | -6.81916 | -52.83451 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 14570ce4-1413-3926-895e-3d5794dc1cc0 | -6.85585 | -52.81866 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bd0d04bc-1b43-339c-bb0a-c5551c9e34cd | -9.83969 | -44.68256 | 2025-09-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ae910a9-431b-3801-a0ed-96ec35986bf3 | -7.91918 | -46.44773 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b27331dd-ba93-3c8d-8951-537b9f1699ee | -9.4861 | -46.50899 | 2025-09-02 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dfd8aa8c-8853-329a-81e5-eafaf8cbb729 | -9.48258 | -46.50839 | 2025-09-02 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f498da0-d6c5-3d2c-b438-9a89a0d857af | -12.87126 | -48.04436 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 477c6011-d563-3624-8b9f-0c579da8b68b | -12.88513 | -48.16062 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8283f78e-5ee2-3d46-a735-329d735ade6d | -8.85649 | -45.79165 | 2025-09-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 518e3eaa-6fd1-3450-ad46-0c66407b849f | -6.49075 | -45.13 | 2025-09-02 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ffff890-4488-3b2a-9c2a-3e36686348a5 | -6.98936 | -43.22847 | 2025-09-02 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1a765c19-acfb-3a51-97c8-a438cab0a25e | -12.95633 | -48.09609 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f75ad157-6d87-3290-862f-fc94858d2b53 | -11.42583 | -55.18206 | 2025-09-02 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7728b6c0-ee87-357b-b48a-318f4e0aa68b | -9.75832 | -49.38717 | 2025-09-02 04:14:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65e43ef1-bdc8-34e9-8d9f-6e09cd609cef | -6.79775 | -52.82541 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7373e62-dea9-32e7-9fec-502d4c0ed5b1 | -10.44569 | -54.772 | 2025-09-02 04:14:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5f6b25af-90e8-3d25-8d42-2c3b826abe90 | -10.04521 | -48.11497 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c457861-7b1d-31af-9170-0fe7d3c22eda | -11.90076 | -44.88134 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68425727-cc48-325a-b3cf-1a66bc142285 | -10.05646 | -48.14071 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 927f8f14-cc82-3b3a-97dd-8a44c48b928d | -10.97057 | -50.77544 | 2025-09-02 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e13f21ab-babe-384e-83ca-dd2a38599153 | -8.28708 | -46.30731 | 2025-09-02 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb65f01b-ca49-3017-840f-5e9369ae1dc4 | -9.97019 | -46.42806 | 2025-09-02 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 54f06fc5-43e2-3aeb-9152-ad8659643071 | -7.9263 | -46.44901 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b4012b3-9d33-3374-95da-17e7b8558371 | -13.46942 | -46.9286 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6f7f157-bd01-34fa-b665-972b930a8d7c | -12.43841 | -48.72235 | 2025-09-02 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6b439a04-1e6c-3a14-a064-9e64d1de479c | -6.97465 | -44.30502 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e46868e-596b-345e-9883-8c9c5c0d713d | -10.83974 | -45.03806 | 2025-09-02 04:14:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75d900b0-58b6-3a8b-b867-77250b9c2749 | -10.26326 | -47.51931 | 2025-09-02 04:14:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6521e3ef-c491-389a-9771-39277c8f9c0e | -8.86338 | -45.7927 | 2025-09-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5725b15f-cc36-3f1f-ae4d-97e8de926717 | -14.05531 | -44.57072 | 2025-09-02 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b195b0b6-9947-3bcf-972f-bc2fe0b48399 | -7.13282 | -44.44696 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ab4f065-574d-3c47-b3d2-2d149c67ce1c | -7.13004 | -44.44282 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d41d09cf-f70a-3041-83d0-b9656bb2cb4e | -10.75221 | -49.5766 | 2025-09-02 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ed6347e-6c59-37c5-bc2e-a16efbef4a12 | -6.78796 | -44.6186 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05b1c7c6-7fc9-3fcf-b9cb-069c025751b6 | -6.91896 | -45.56303 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 30f89e8d-b475-3316-90f3-e95da4950ae2 | -7.62036 | -44.93641 | 2025-09-02 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2afb442b-1956-3f6c-9049-0a6a7653317a | -6.96115 | -44.3464 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59714ed7-58d4-3b19-8120-1c8ec7224c11 | -13.27783 | -46.89309 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 230386da-a910-32b0-8f6c-15921887729c | -10.833 | -47.45425 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a20a746-5305-37dc-89af-bb36cbaea341 | -7.4955 | -45.35867 | 2025-09-02 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b76e638-a266-3413-8476-10ecd07076bc | -11.53928 | -44.84734 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README38.md)
