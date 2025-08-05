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
| 1a464ee6-3b6b-38b4-af13-bba814763bc8 | -11.75332 | -45.01719 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee920ed8-a8ad-3448-bc29-67b6b8231b8d | -8.0036 | -43.1429 | 2025-08-05 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 04471e54-59c7-3f27-b396-6cd9278d7806 | -11.75835 | -44.96467 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c678c544-3b26-303b-ace6-b7338f5a248b | -7.99168 | -43.16163 | 2025-08-05 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| dd962c51-20b2-35e9-8631-6f5f44aa1285 | -8.39199 | -46.56128 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a08f6c20-2926-33b7-8425-017b17dcffb8 | -12.67341 | -48.12637 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 52498ac5-3135-316a-9cbd-32fcc0757e18 | -11.93253 | -44.96158 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fc9b320b-8848-30c1-8d90-f9aaaf1585c0 | -8.91447 | -48.93243 | 2025-08-05 03:49:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8d8dbf3-9951-342b-9071-9715369e754e | -10.34093 | -44.90736 | 2025-08-05 03:49:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 83064454-4b51-3881-a9ca-8a6d273a9a30 | -11.81408 | -44.2579 | 2025-08-05 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 601bf973-db99-37f8-8828-6d748a7df64f | -8.01899 | -43.12916 | 2025-08-05 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1146347b-ecc5-3716-aa55-3dab31f26d69 | -5.98627 | -49.91006 | 2025-08-05 03:49:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a35efc24-a768-3f7a-a310-f623786c527c | -6.23015 | -45.86086 | 2025-08-05 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 41f2967d-aed1-3e5f-8a8f-ba26730f3d53 | -12.68838 | -48.07754 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa915d64-8cb2-3c26-917a-7164219b7dbd | -7.90441 | -45.53528 | 2025-08-05 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3e9ad6a-4ff5-327e-939a-ef402689c900 | -12.67439 | -48.12687 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 11ee8fdc-9467-35ed-bfdc-24b6bbd93421 | -5.98796 | -49.91095 | 2025-08-05 03:49:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3b861fd8-aec7-3cbb-ae25-c40bbce5a5bf | -8.24431 | -45.0619 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| adbdc7b0-03fe-38af-bb62-4e5ce11edfb5 | -12.54654 | -44.72543 | 2025-08-05 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d1a2ccc-9cd5-3763-b25f-620a15845dbd | -6.92896 | -43.34186 | 2025-08-05 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aa9404ee-dd1d-3387-86f9-855df1be073f | -7.214 | -41.8538 | 2025-08-05 03:49:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| da7b304c-1676-3db8-9abb-21ffaaa6b2cb | -9.30041 | -40.24329 | 2025-08-05 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 596329fb-0a7e-3325-b347-df19014ae242 | -10.44866 | -44.36649 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76287928-dec5-35c0-82d2-49a2ddfbbd7e | -12.68091 | -48.11664 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 820dbaaf-c54c-36cd-8cf7-ddca0f27624f | -7.99099 | -43.1657 | 2025-08-05 03:49:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 936c7755-eedc-3a15-b79f-4b970d684463 | -6.38232 | -43.71496 | 2025-08-05 03:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4206fb2f-9506-30a8-8b92-6420457579d8 | -6.37699 | -43.71895 | 2025-08-05 03:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0c089dad-1aa5-346e-b495-86639cf3b139 | -7.83011 | -45.22812 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6a6fae7-19be-31b0-8c47-c254d8256867 | -8.25311 | -45.06526 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68528948-3a79-3b5a-8943-7307b0211151 | -11.75122 | -44.99338 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6f0c44b-4cc0-32d1-b469-1af73f474524 | -7.69644 | -41.24642 | 2025-08-05 03:49:00 | NOAA-21 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e6f6c6f0-6f09-3035-a1ad-29ea7b1a981f | -8.93786 | -46.74317 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4607ef62-7802-3520-a3b0-86faf8ed4997 | -11.74777 | -44.99685 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e4fe517-3ac2-3c66-b679-e17687ab65cc | -11.03977 | -47.61542 | 2025-08-05 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0fee7709-cdca-3132-9e92-74f6677dcf27 | -9.39595 | -45.50942 | 2025-08-05 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6a03d5c6-32a7-3219-8939-9747f3ad40f3 | -7.11915 | -47.84399 | 2025-08-05 03:49:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d147819c-e662-326a-b1a0-81b33827b344 | -8.74739 | -46.41753 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a600703-bf6f-3f86-b3cd-d02e65048966 | -8.00003 | -43.13828 | 2025-08-05 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| ebd820fb-50cb-30f3-bee6-ca04a1e50480 | -12.35038 | -46.05806 | 2025-08-05 03:49:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5440cd1-cba3-378a-861a-e994366df226 | -11.929 | -44.92996 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 66b2c651-ec72-348e-81d8-0a292c874198 | -12.5107 | -47.18455 | 2025-08-05 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 30c24162-851b-37e2-a97c-480454008465 | -9.40373 | -45.49411 | 2025-08-05 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0aa6b74-9da7-3e01-af1a-0d8640025c69 | -13.82007 | -43.69063 | 2025-08-05 03:49:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24962849-e6f3-3408-8ba9-6920d7195c4b | -7.71291 | -43.91182 | 2025-08-05 03:49:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9af65c96-6b04-3a08-a878-43b94200f363 | -9.39694 | -45.50398 | 2025-08-05 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| aef19464-952d-3755-b68b-fd01d674f85e | -8.24044 | -45.05571 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e905301-a05f-3b8c-8116-2a8dc21c1791 | -8.94299 | -46.73755 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 719fd422-45d8-3399-be67-be218dc42b01 | -9.33325 | -37.98247 | 2025-08-05 03:49:00 | NOAA-21 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 91d86476-07b4-364d-8d57-9d06586c9015 | -11.04517 | -47.6165 | 2025-08-05 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e5a01ac4-398b-333e-82f8-80a433948c49 | -6.96885 | -42.86478 | 2025-08-05 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| a19292a2-6801-38d9-9bc5-5623afa67170 | -9.05295 | -45.05965 | 2025-08-05 03:49:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 369f2090-60ac-3068-918d-86ac12ae7c0f | -8.71304 | -46.42877 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8046b39-31b9-3c10-8e75-a4e72f0fa9db | -10.52943 | -42.54826 | 2025-08-05 03:49:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 4279bcd0-76de-3209-855e-cd6265173f1c | -8.23952 | -45.06102 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7588779-8af7-3c93-a5a2-34f51d401e86 | -11.76653 | -44.97066 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c928b36-a7f8-3688-84b0-e0d2fc3ecd00 | -11.06777 | -48.35833 | 2025-08-05 03:49:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 703d79e8-5f0d-360b-a40b-265c77274231 | -10.44621 | -44.38004 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e85a160a-840b-31d1-b44c-b54f02a0f2a4 | -10.44946 | -44.36205 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7dc2af38-53e2-3ad6-a1ab-7dae87a8b83b | -12.68197 | -48.11712 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40ee2e5e-aa6e-343f-8715-c3ee89045fc7 | -8.39259 | -46.55796 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e38805eb-1080-30da-a758-a6b61d634e99 | -10.44802 | -44.37261 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0081887-6e3f-3aa4-b72a-3780cd8117d9 | -6.42558 | -44.8185 | 2025-08-05 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aee55366-3eac-323a-86d5-89e15eb7600b | -9.17942 | -48.84289 | 2025-08-05 03:49:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6456f80e-ec5a-350c-913b-9e1372430b8e | -11.91656 | -44.97326 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 42eefd97-2867-39d8-a9e6-4890911d7e37 | -7.90343 | -45.54085 | 2025-08-05 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb593413-23ef-3ce3-9c0b-56379dde0d5c | -7.14003 | -44.08286 | 2025-08-05 03:49:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4de7d44b-4f23-3291-9322-d0042ce2f8bb | -13.37264 | -43.75951 | 2025-08-05 03:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 970f2d10-a99c-3840-9a5b-31236a5f1fc6 | -10.77894 | -46.64429 | 2025-08-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c228bca-69ce-3727-9d3a-6b460179fd49 | -11.7459 | -44.99721 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| afb322f8-b2bd-3682-8070-02c3c43c704b | -11.16099 | -49.69997 | 2025-08-05 03:49:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2cba79c-5a16-3d81-ae1f-01640f11acbf | -11.0445 | -47.61995 | 2025-08-05 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a05540c6-3744-3930-b9d8-17376bbec182 | -8.26368 | -45.06157 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f76acd6-a062-39fc-a4b7-345e00eb94ec | -8.71829 | -46.42957 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3aaf4e52-032c-32fa-aa5b-d50b2a2a7e62 | -10.46552 | -44.37395 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9532146-4cda-339a-9f09-476a585d1823 | -8.2155 | -45.05688 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93e232a8-a494-3c1b-88bb-de92f6b5b975 | -6.38154 | -43.71959 | 2025-08-05 03:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1965250f-2509-3d0d-936e-f7325d8f4ed7 | -8.24446 | -45.05832 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 856ae13c-91bb-3fe2-920b-eadc320e7a7f | -11.27692 | -44.64838 | 2025-08-05 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d767c41-0ae6-3c9a-8d37-52178b67f388 | -12.42709 | -44.70512 | 2025-08-05 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a27de04d-953a-3cd2-b474-47542e81030f | -10.32703 | -47.82809 | 2025-08-05 03:49:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 40fe5721-2009-337c-86c5-49c5f86b4d8e | -8.01342 | -43.13638 | 2025-08-05 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e705910a-48ed-39b7-8196-62b46a3d38eb | -11.04364 | -47.61613 | 2025-08-05 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2f39dc0e-f020-3ccc-8206-a199d95f3217 | -6.5016 | -42.80122 | 2025-08-05 03:49:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1f4cbafb-9b58-3a26-940f-a34a99b0f9a0 | -7.78412 | -45.21803 | 2025-08-05 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d82d4cd6-4018-3dea-99bb-b734c4829a66 | -8.25393 | -45.06353 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a7e466c-fb71-3579-bcc9-d1a53cce39e4 | -11.04906 | -47.61711 | 2025-08-05 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 34c65b09-9d52-3bcf-89ef-0e7b59b65104 | -8.27328 | -45.06322 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ea3ef5d6-337c-3d67-8a05-65cd6aafd721 | -8.02003 | -43.1746 | 2025-08-05 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 6f435512-127f-3dca-aa49-253bae20c690 | -10.47075 | -44.37016 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8cd932e-bf68-357d-87d3-097e0084cae3 | -6.4668 | -43.03127 | 2025-08-05 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a63f0ea6-9ba9-313c-8acf-83cbfb91f1fc | -5.9852 | -49.91598 | 2025-08-05 03:49:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 22dc4949-a873-33b7-b560-961fa630f33d | -10.46387 | -44.38311 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ca6911d-c492-37de-84ff-276daeb7b194 | -12.3456 | -46.05717 | 2025-08-05 03:49:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7b277c8-6ca1-3eac-a713-4baf03e086bc | -11.15558 | -49.69906 | 2025-08-05 03:49:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6b37def-608d-3ec7-9e31-5800ceed13ed | -12.99055 | -47.45773 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d4c9708-4481-3032-872f-6ab04c3b3d2c | -11.04299 | -47.61963 | 2025-08-05 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5832367f-d594-376c-9bb8-90a850a5070b | -11.74882 | -45.01635 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18a79d9a-244a-3c30-9b41-f78a5037e7d9 | -9.05773 | -45.06025 | 2025-08-05 03:49:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f84c41ab-c066-3b14-8eaf-413da8ba8a29 | -12.51525 | -47.18859 | 2025-08-05 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03f894ac-936d-3a17-9731-10e739456d93 | -8.23472 | -45.06017 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README11.md)
