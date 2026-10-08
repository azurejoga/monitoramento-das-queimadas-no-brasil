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

## Dados Diários - Página 242

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c35db64-6a6d-31d0-a49b-274468b28e92 | -7.00602 | -43.674 | 2026-10-08 15:41:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 519d6f67-7289-3706-8688-6aa3cee11bd3 | -8.06805 | -45.61611 | 2026-10-08 15:41:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| ac87177e-a054-366a-8eb8-0f5fd4e87196 | -5.51151 | -42.82946 | 2026-10-08 15:41:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 29eda65b-1217-3d02-a856-1fd59b1431cd | -9.04116 | -46.60247 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 8b87635e-0e57-3233-892b-133d05448881 | -7.34417 | -45.27805 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9e74e919-346a-30e2-925a-53ea4dc47158 | -6.93008 | -43.06806 | 2026-10-08 15:41:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| edb1deec-0f22-3065-a81e-8cf78a5d6606 | -11.20509 | -45.21129 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 03a53af3-8878-3664-aa48-e99130318b54 | -8.94194 | -45.14181 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| ab047298-dd9c-3415-ab93-645a0111e5fa | -6.65116 | -43.76443 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| af4258eb-70cf-32b7-b02e-f54f47975d98 | -5.7729 | -42.0503 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 8955c6ac-62cd-385e-8f9f-de45fd16f869 | -6.16155 | -42.58448 | 2026-10-08 15:41:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 1b3d1f25-808d-3f16-a8de-a3261514ebbb | -6.52605 | -43.54 | 2026-10-08 15:41:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ef5d140a-761c-3ca9-8fd9-2a58fde6a8d5 | -6.57188 | -41.61543 | 2026-10-08 15:41:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| cf08b23c-9da1-367c-b27a-3f5998d5f7d3 | -5.72713 | -41.6426 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 63913792-b599-3355-bc54-0336664456ca | -5.94922 | -45.69835 | 2026-10-08 15:41:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 97ff2825-e1a6-33e6-ac85-5de549ccb093 | -5.47872 | -44.60761 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a69e3fb4-7b2b-3b62-b5cf-f3203214b6c3 | -5.27829 | -42.7346 | 2026-10-08 15:41:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 50.5 |
| 22bdad86-97a9-30fa-af8d-4264bb811fa8 | -10.60552 | -43.84605 | 2026-10-08 15:41:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 8f7e51e6-255a-3218-8224-62a7a71d79d3 | -5.28455 | -42.74027 | 2026-10-08 15:41:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| afd63fd4-8465-3132-8f55-b9d225d8655b | -10.58226 | -41.20544 | 2026-10-08 15:41:00 | NOAA-21 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 38.1 |
| 1d96ee23-7c6e-3a9a-80f2-e2c91d565987 | -5.23697 | -40.57816 | 2026-10-08 15:41:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 5a0d4dc1-af67-3b51-aaae-cd4684cc2af3 | -10.38046 | -46.31928 | 2026-10-08 15:41:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 125.3 |
| b65f31b9-800f-339e-884a-b82646ad0e11 | -6.68866 | -41.76299 | 2026-10-08 15:41:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| f50cd879-4a95-316f-9234-ef1fb2933f1d | -7.00414 | -43.44208 | 2026-10-08 15:41:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f9321cbe-f2f0-3a22-b8b6-bbd118794d0b | -7.81921 | -38.85774 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 9e0f865a-df89-3aa6-9220-10bd49cf291e | -7.63812 | -44.38095 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 36.0 |
| e47e96b8-67db-3d1f-9ad5-9a815c0ab01e | -6.95498 | -44.41919 | 2026-10-08 15:41:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ac254b10-be17-3e75-87d2-99249ba4c4c0 | -6.84636 | -39.55711 | 2026-10-08 15:41:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 1077cfe1-0240-329d-8b24-9e73a53edd06 | -5.54423 | -43.22293 | 2026-10-08 15:41:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 0a3e205a-006e-3ee0-8e7e-ec2fed1656cc | -6.20436 | -37.87857 | 2026-10-08 15:41:00 | NOAA-21 | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 7.5 |
| aba2cb89-3f5c-31bf-8aab-646e477843f7 | -6.84885 | -41.7691 | 2026-10-08 15:41:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 915f822c-13c6-3544-aa35-2080d8ada549 | -7.10179 | -41.74327 | 2026-10-08 15:41:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| c5fb27bb-70c5-3cce-97ca-5e2c4173ca50 | -8.37295 | -44.76715 | 2026-10-08 15:41:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fa7b4639-4fb7-3d91-a1a7-e799247276ce | -5.74652 | -41.59896 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b06aa094-6c3c-35ec-9dd7-21b7ddb27891 | -10.98672 | -45.40236 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| b766acea-ecc8-307e-9938-5cc60a277693 | -5.53621 | -44.28813 | 2026-10-08 15:41:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 1f2a1058-c102-3d7a-a043-f8fa2d5dbe21 | -5.72292 | -41.64908 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 30.2 |
| f18a604a-85b6-3332-8093-182d24687199 | -11.05328 | -45.84891 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 002a5b92-6b7c-3e89-b666-5d7180a40c14 | -6.72968 | -45.18246 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 39170e08-e041-35d2-8abe-5953ff7988a6 | -6.95373 | -45.27618 | 2026-10-08 15:41:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 61a0775d-fdca-3e3f-969b-482778d3dfdc | -8.95578 | -45.14571 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 49.3 |
| e8ef1ae8-a476-3850-94b3-d0a3ad94f77d | -6.33386 | -43.35476 | 2026-10-08 15:41:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 593ca132-97f2-38a5-b741-83d6b76d6d0b | -11.2572 | -45.18706 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4de8b922-3ba8-3904-b65f-dde450cba7c3 | -5.26504 | -45.40866 | 2026-10-08 15:41:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 0f299a5e-1641-3703-b430-a652c87c8b7b | -5.71773 | -41.64964 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| ade86f7b-64ef-3d06-b1b4-0904dbde3fb3 | -11.09289 | -44.01007 | 2026-10-08 15:41:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 82965829-c46b-3b5d-86f9-e4f5383bb681 | -6.15907 | -39.42921 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 0cf52ec8-81dc-3290-a901-0345e442b889 | -6.8233 | -39.55426 | 2026-10-08 15:41:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 76ff978d-d852-379a-8ff4-291175185565 | -9.82897 | -45.76204 | 2026-10-08 15:41:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| a0225f60-6ec0-3ae1-9aaf-aeb4056c983f | -6.8231 | -39.55129 | 2026-10-08 15:41:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 8964bb7a-7995-3493-9935-30116f150d40 | -5.76678 | -42.05962 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 0887a549-1c9c-3e87-b039-a05f29b6c46d | -6.35902 | -42.5656 | 2026-10-08 15:41:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| 8cccc3fb-8fb6-362c-b398-0c793a38df95 | -6.57653 | -41.61172 | 2026-10-08 15:41:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| e958a252-32c6-31fc-a689-ccb8178c2e94 | -11.11179 | -44.00808 | 2026-10-08 15:41:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 2a2a3349-5b0c-3bad-b1de-5c1aa7de09dd | -9.14199 | -45.82812 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 34.2 |
| c99e1472-2eec-3d8b-b73c-3c0a49b8c328 | -5.75396 | -42.0802 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| d7bc7dc2-ce09-316b-88a6-db165ce3d346 | -5.74183 | -41.71186 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| d706b8ac-668e-30c2-8300-bfc4054b481a | -10.16234 | -45.97151 | 2026-10-08 15:41:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 2c36414e-7981-34cb-9eb4-2af55f1ee47a | -5.72584 | -41.77619 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 4406793c-2a6e-3ad1-b858-f83ec664720c | -8.21641 | -46.41656 | 2026-10-08 15:41:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4f465762-5c76-3492-a5c2-1471ef454e66 | -11.20723 | -44.87373 | 2026-10-08 15:41:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 01d634aa-2ff9-3fa4-b4e9-c613101d971e | -6.53718 | -45.38375 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 9ee8a916-12b3-3b31-82d4-7e5d67c02801 | -11.11119 | -44.00304 | 2026-10-08 15:41:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 18ad3eec-b447-310a-bf11-aed9121a0e8c | -5.3699 | -44.18923 | 2026-10-08 15:41:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| be4e5ddf-dce6-3729-be54-6fc1ba081a8c | -10.2283 | -40.04744 | 2026-10-08 15:41:00 | NOAA-21 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 8390739f-80d8-387e-bbb3-8448b26d0d4e | -6.42888 | -43.82982 | 2026-10-08 15:41:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49b86eae-1352-3cad-8656-97091f050e67 | -5.7094 | -41.73358 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.0 |
| 82221589-1e3b-3607-9ae3-35ddf5ade961 | -6.45504 | -46.01634 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| e87ce1a3-1d5e-3286-94bc-7f5900d65972 | -9.90041 | -44.82284 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e00621c5-bcb4-39d9-a8c7-5b22244fcd6d | -8.88876 | -45.39724 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 41.7 |
| b1ebbc72-dc12-339f-930e-a4d8ccff1f8a | -6.96271 | -44.99492 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 67348225-21d9-37e0-9438-416bd1395d80 | -6.77117 | -44.12515 | 2026-10-08 15:41:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8f14af38-cbf7-376b-98c8-b8d8947839de | -8.598 | -45.63268 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 31a7c6bd-29b2-3967-85de-4310619f81d6 | -5.98638 | -40.9399 | 2026-10-08 15:41:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 4daa0ff9-1e68-3d1d-a1a3-f4b417422763 | -7.78976 | -44.58143 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5adeb714-f33a-3cd2-8f94-409c3e1d70a2 | -6.34635 | -43.83623 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6faffc57-14d4-3600-a7ce-9428e2ff1b30 | -5.28409 | -42.73699 | 2026-10-08 15:41:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 50.5 |
| 6ed0f0c4-f143-3420-997a-a6450d88438c | -5.77105 | -42.05281 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 2ddb456c-48e7-3834-b8ab-2fd1d8112d26 | -6.63402 | -43.77454 | 2026-10-08 15:41:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 93378afa-bf91-3550-9db7-cc16dbe8b3b4 | -5.74718 | -41.64005 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 629e7d34-dde1-3dd7-a49d-831df012b80c | -11.11493 | -45.96594 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| ac1d097b-2732-39ab-88e6-485c8cd8710d | -5.7762 | -42.05213 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| b7d04c60-87c8-3fd7-a46f-5d72e2e3090f | -7.04429 | -44.33268 | 2026-10-08 15:41:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 4d1c73b7-377d-3493-863b-b337234d6862 | -9.36004 | -45.95071 | 2026-10-08 15:41:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| db3350cc-b344-3ff2-93a4-304d945d4e95 | -6.94131 | -43.0666 | 2026-10-08 15:41:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b91d4a1d-71dd-37ea-ba92-6b418f99259e | -7.81881 | -44.5758 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 82798ef0-d894-399d-9517-3f46e5e2c3ff | -5.45704 | -45.58949 | 2026-10-08 15:41:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4b508302-d6fd-32eb-8d74-3782f4a3c23c | -10.30763 | -42.38019 | 2026-10-08 15:41:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| d145ebac-1cec-3846-8c04-a1b03616254c | -6.36785 | -42.52667 | 2026-10-08 15:41:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 03e7a1d4-3d02-3390-a782-8f761cf25851 | -11.27217 | -45.19785 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 78bff3c2-1e7b-37fc-ae69-dcef19a1ef76 | -6.1504 | -39.43025 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 907935f5-9aac-37ba-9023-7a8d45fb722f | -10.87184 | -45.55289 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 39d32762-7250-399a-8fba-a967d64c2fa9 | -6.12849 | -44.14587 | 2026-10-08 15:41:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 44b655c7-5943-3e90-897c-b0a0b8e81f43 | -5.9133 | -35.38124 | 2026-10-08 15:41:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 85a692fe-843a-301b-9662-76c78adb199e | -7.08524 | -43.08707 | 2026-10-08 15:41:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| e2ece986-6b10-3a13-bf31-a47ea9f0cebc | -7.69698 | -45.44231 | 2026-10-08 15:41:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 517c2d3d-bd7a-35c1-8c25-5575e2099773 | -4.76943 | -39.02623 | 2026-10-08 15:41:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 26.9 |
| 145da301-2ab2-3794-802a-8203846a51e9 | -4.90879 | -42.47358 | 2026-10-08 15:41:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9955a559-7409-3e6f-9779-340392928239 | -5.7488 | -42.0809 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| e0395d21-de22-36ea-86cb-9981237e2e5b | -6.15416 | -39.42556 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |


[Clique aqui para ver as próximas entradas](README243.md)
