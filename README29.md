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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74caf1c4-284f-3681-8448-a19dd57e35f3 | -5.55803 | -45.3373 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a908019-197f-344d-a885-ce56f3a0ed42 | -4.31808 | -48.62985 | 2026-09-30 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 78410185-ed38-3638-a71d-9e464ed9f6f6 | -8.83087 | -49.71524 | 2026-09-30 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c9e2f156-d792-3442-a627-957319604541 | -8.84087 | -49.70468 | 2026-09-30 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 36d1373d-9402-3e5e-ac96-5cf3ad5d4ed2 | -4.84317 | -42.87892 | 2026-09-30 04:32:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1cc23ca-aca0-3f51-a35a-a9f3af2a4ea7 | -3.37527 | -50.84785 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4fca2495-e45d-3843-8372-869711de4f75 | -3.2224 | -46.94916 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5ee8c41-70d1-39d9-8f61-3cdb5a785627 | -5.75111 | -45.1736 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e16138d6-d5b6-30b8-8bba-e09299df1a3d | -7.27597 | -44.30204 | 2026-09-30 04:32:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe9607ae-b255-317d-957a-58b347bd5b6c | -4.81402 | -45.63833 | 2026-09-30 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 436478fb-3527-39fd-bac4-84897d21f446 | -9.66453 | -45.1154 | 2026-09-30 04:32:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b40ed404-5500-3375-832b-872a69c25263 | -7.19863 | -40.11914 | 2026-09-30 04:32:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d1f6179f-99b6-3398-9603-22f414a90f56 | -3.37408 | -50.93975 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5ef239ac-2a19-3afc-9180-8b4d9ccf9870 | -2.3806 | -50.40869 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4aa9356f-f9c1-3010-b3da-92b4e3f68858 | -6.33902 | -55.32752 | 2026-09-30 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91c02f3a-859e-3b4d-9010-b70802d79d84 | -4.12797 | -46.87191 | 2026-09-30 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e1b6585f-6e72-3bb0-a9eb-fa93643fe6cc | -7.01971 | -45.30078 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bae10fb-88ea-3817-94d5-b4c8b575be3e | -6.33162 | -51.16512 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 23ae5abd-3f27-399b-b977-943c3c5b549d | -8.17636 | -44.42958 | 2026-09-30 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97635903-e747-375f-b360-6e7d09bbd948 | -6.52709 | -47.12071 | 2026-09-30 04:32:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ada7cd3-f00b-3e59-9df4-177f88062eaa | -9.04262 | -47.3261 | 2026-09-30 04:32:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b37345d2-bf18-3041-9a5a-786595cd98c8 | -5.5586 | -45.33378 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fefdb16f-1aa7-319b-99ae-0349fe29c0a3 | -6.71553 | -45.6553 | 2026-09-30 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17021884-be40-3af9-a396-c211ffdbf37d | -3.38172 | -50.95097 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4db48a7d-66e1-3736-82aa-b082093a99b6 | -3.18182 | -51.24105 | 2026-09-30 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| eac06360-66e5-3831-b5d6-1035bff0598d | -8.00604 | -44.49992 | 2026-09-30 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a9fb077-9d01-38b6-a2c4-8720b0235c79 | -3.95396 | -49.04906 | 2026-09-30 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddf4a850-da81-3288-9950-c9bab3a2de3a | -7.93319 | -47.37284 | 2026-09-30 04:32:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ccb5799d-fe18-3da8-998a-4e956427bfc8 | -2.79078 | -49.41162 | 2026-09-30 04:32:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9790019a-7e3e-30ab-b380-3f023d372e31 | -7.8437 | -45.82217 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f65c320e-e0d9-3846-912f-bd43b93c178e | -4.02331 | -54.20622 | 2026-09-30 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07d5d72a-3e2e-3e55-b2d4-f60031cfd14c | -5.16493 | -45.26021 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50af8c3f-0a93-3ad4-a866-1e2e980922c3 | -6.32944 | -43.913 | 2026-09-30 04:32:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2045300-f9ca-38af-9cf8-ae9d5887924e | -3.91613 | -49.37457 | 2026-09-30 04:32:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dfb6ff4-2ea9-3cce-8620-97e9c1a105e3 | -7.53828 | -47.12091 | 2026-09-30 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 93b5b598-3501-309c-9d44-ebcce0908815 | -7.81577 | -45.82497 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 20183192-74cd-3256-bcc9-5f3a8b41c009 | -2.9709 | -51.03768 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 63c3ec8a-5b9c-375d-8ea5-df1a0c227ad8 | -6.18363 | -44.64648 | 2026-09-30 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a2d4f035-bc64-3ab5-b904-e5b454a6d0c0 | -4.32199 | -48.63047 | 2026-09-30 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61bc0645-9da9-3fb0-a959-7f35e7af82a6 | -3.04839 | -53.86543 | 2026-09-30 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4feac89b-f5ec-33b7-8b16-e8c57ff9719c | -9.12617 | -44.74903 | 2026-09-30 04:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a8ec409-6482-32e7-b17a-5b27809611de | -8.83223 | -49.70826 | 2026-09-30 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b57fe6a-823c-37d6-8eab-453c177d57b5 | -3.226 | -46.94979 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 345bdfdb-6d21-3abf-abb7-6de11f8217c6 | -4.81286 | -45.64554 | 2026-09-30 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ce1d77fc-d850-342b-a4d9-d288bb2b5968 | -6.17837 | -53.28473 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c45a4796-f5fc-369c-afbb-10ce2a4d49c2 | -7.08108 | -41.74805 | 2026-09-30 04:32:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 535cf01d-e35c-3ce2-a4f1-cc8047d4ee50 | -11.40532 | -43.41398 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3643dff-1358-3ec9-a2a9-eb9b27ae9d8f | -9.9311 | -50.15083 | 2026-09-30 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c023f767-fdb9-3e9f-8fea-01765bbc9668 | -10.70644 | -50.83849 | 2026-09-30 04:34:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 026c0942-b157-3f00-b88e-a5152f537783 | -12.75904 | -47.25023 | 2026-09-30 04:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 733627b6-a3c5-37e3-8b72-38a153590196 | -13.36619 | -46.82254 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a281c9e-63f3-3123-9c70-09f092863cd6 | -11.45885 | -43.46231 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3666625-72dd-3c2d-8c56-b21b95b93bfe | -14.50688 | -48.28576 | 2026-09-30 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4001b239-442e-3e53-aace-de41dd5298bf | -10.66168 | -50.74157 | 2026-09-30 04:34:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6a19f34-a185-393f-bfbd-433dbf52a618 | -9.79241 | -44.81472 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96d5c88f-258d-30ca-9051-e7c0c2c9f140 | -15.20433 | -46.12943 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3783fd78-4642-3130-b4cf-d9e967b15fd3 | -9.80411 | -44.82744 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bed25721-a55d-35c7-bc5b-25aae359b7ff | -11.19737 | -44.82212 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5043100b-4361-3dbf-b055-a0c4619e3780 | -11.84087 | -50.97358 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b8fabdc-cc46-37b6-8a86-3911d25bcda8 | -11.84553 | -50.97074 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d3ed20f3-ab1e-3adf-8060-2c128043154d | -14.91009 | -41.68934 | 2026-09-30 04:34:00 | NPP-375D | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9b917cd9-d929-3efc-886c-3a4fbc8b3f72 | -12.2191 | -44.27446 | 2026-09-30 04:34:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2f97129-cd7a-3c6b-8bea-352014c9462f | -15.79023 | -44.68928 | 2026-09-30 04:34:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7999b3a-95b5-3a23-9b33-c9c9f221f52d | -13.37896 | -46.82834 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dd0f47cd-710f-331c-a347-2eb964803097 | -8.48452 | -54.91 | 2026-09-30 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69ce8ab1-c4b3-3fb4-8394-3928b1c57a1b | -8.05816 | -55.34071 | 2026-09-30 04:34:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aab6cea8-3f4c-3690-83c2-2723329cf061 | -17.10061 | -46.4732 | 2026-09-30 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5da67e80-32f9-311c-92c4-580997e34779 | -10.90315 | -43.85681 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20c6092f-5812-3556-918c-c693abf1fa80 | -16.29029 | -43.66373 | 2026-09-30 04:34:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 887916d0-7663-3062-ba95-cff8c140c6e4 | -11.38857 | -51.01076 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2366d8db-62b2-32fd-9d35-18cef75e72d4 | -16.35786 | -42.58681 | 2026-09-30 04:34:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8912045e-5172-3cdc-89f3-ab407d50de7f | -14.12569 | -46.26147 | 2026-09-30 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 25326afd-26ee-3d92-b9a7-faf65cb56b3d | -10.83239 | -48.70121 | 2026-09-30 04:34:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5e51ffa0-de4a-38b2-b8e8-cdf09a006287 | -9.92629 | -50.15522 | 2026-09-30 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da6c95ca-a83e-328e-bc4f-b790b6b1a474 | -12.44079 | -44.1662 | 2026-09-30 04:34:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 590fe291-03f7-38b6-8081-254eaea1b1d5 | -14.10347 | -46.27239 | 2026-09-30 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8b31b8c-45fd-3a3f-8da3-db41dec34049 | -11.36664 | -43.35682 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6cc04c0b-bb65-3703-90bd-5123826f007c | -11.84491 | -50.97432 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f9ee7ef3-2d3c-3458-89b3-42cbf9a5bd0c | -12.34286 | -48.19865 | 2026-09-30 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95ef79db-a345-34bd-af0b-3ba1a6c3fa4d | -11.83997 | -50.95492 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 92940cf2-28a2-357d-96a6-4cfda98eeedf | -17.57263 | -43.70789 | 2026-09-30 04:34:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8fb93cd-87e1-382f-b95f-cb683c559d5b | -9.79854 | -44.81932 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29b225c5-288f-3e44-91ae-1ecec82b4b8f | -12.59961 | -47.23904 | 2026-09-30 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ca185d1-0e4d-3f97-9453-157ce8f293cd | -10.11213 | -43.92262 | 2026-09-30 04:34:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55ed8907-fc11-308f-aaf5-39c5e3fca94d | -13.55785 | -53.2063 | 2026-09-30 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e0175016-9848-3d2a-812d-36ef9c025439 | -11.38321 | -51.01733 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 149828f0-8099-30a1-b18f-a56a36109a62 | -9.073 | -49.86987 | 2026-09-30 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c92a97e4-a769-3b3e-8f3b-e53251dab01c | -11.85546 | -50.96151 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70c33b1d-4342-3f30-bdfa-1f70b79d4fcb | -12.62596 | -48.35775 | 2026-09-30 04:34:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 16fea811-de29-3cfd-8d60-0583be9df4f4 | -13.36789 | -46.81195 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7a35893-01a9-39e4-a843-219928c58e5a | -11.38921 | -51.0071 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 698c82aa-e630-3ac1-8375-beba2ca8ed2e | -11.42454 | -43.42899 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8092bedf-c621-32bd-bb12-6c72f23dc6e7 | -11.63503 | -43.53612 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18e8a340-3a72-3491-a6b0-ec68c66798f7 | -9.86037 | -44.96324 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03448c40-2944-3198-8da2-20504ac2305f | -12.63079 | -47.24387 | 2026-09-30 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8809a1e0-9493-3667-8362-1d85da12865c | -15.09227 | -47.83021 | 2026-09-30 04:34:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6db644d0-9c10-3ef0-a90b-0d9042230132 | -15.25552 | -44.81848 | 2026-09-30 04:34:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25fe0569-ab8f-3c30-8b67-8a7a3dc79d4f | -12.56801 | -43.06969 | 2026-09-30 04:34:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 05e096c8-38f3-336b-84a6-ad5586abf796 | -12.31797 | -47.95436 | 2026-09-30 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b2b9ae0-3d97-3e89-a576-ec59e1168f2b | -11.39392 | -51.0042 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README30.md)
