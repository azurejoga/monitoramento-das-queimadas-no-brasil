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

## Dados Diários - Página 215

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5af4a92-3578-35b5-9cea-adadf03b5e63 | -3.88216 | -44.10315 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 44a02020-bad2-36eb-874f-d1772416dfee | -5.37017 | -44.17189 | 2026-10-07 16:37:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5a0a58d1-d0e5-39f5-a4c7-996e454544ea | -6.93338 | -38.2947 | 2026-10-07 16:37:00 | NPP-375 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 03200c35-4f42-32b1-ad6a-68e87f8a7cf6 | -5.74215 | -53.47131 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 654cb7f0-5f51-3f32-9b3e-68fa90621582 | -9.87001 | -46.31445 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9016e746-a235-3b5e-bcc0-86ca02d7a404 | -15.9632 | -40.70513 | 2026-10-07 16:37:00 | NPP-375 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e73ead8e-9b62-32bd-909e-4fff64205de3 | -5.85531 | -42.66177 | 2026-10-07 16:37:00 | NPP-375 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| d0b2e3a5-6219-3671-a25c-3ba5187f0550 | -3.43827 | -43.26147 | 2026-10-07 16:37:00 | NPP-375 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| a03308bc-441e-3203-8174-39d09aaea3e1 | -6.92668 | -41.23595 | 2026-10-07 16:37:00 | NPP-375 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 306e6b6c-2335-32e6-8726-c56a57db5755 | -8.76899 | -44.16014 | 2026-10-07 16:37:00 | NPP-375 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f5f66c8c-33bb-3aa0-982e-e7745488ccc5 | -5.86342 | -51.16498 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 7a33accc-0c5d-3177-8568-cef853a87658 | -16.46811 | -39.08854 | 2026-10-07 16:37:00 | NPP-375 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 62ada379-6bc7-35cb-8f7f-b0b577ff9faa | -4.42015 | -43.7352 | 2026-10-07 16:37:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| b7e2f47a-ef26-3f15-9eac-89649dc5b1b8 | -16.90644 | -42.11767 | 2026-10-07 16:37:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ac0c603f-3321-3275-89a8-e08a8b4dddbd | -3.93154 | -42.73011 | 2026-10-07 16:37:00 | NPP-375 | PORTO | PIAUÍ | Brasil | 2208502 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| cd3fabb4-983d-36bc-989c-263ff7ec606b | -6.78419 | -50.91898 | 2026-10-07 16:37:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1d11507e-b881-3e90-b57c-82c09794b283 | -3.75492 | -41.70708 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a17edd3d-9854-30ab-bc24-f548b77defc1 | -6.19336 | -52.83355 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9c1daac2-4ee6-3655-ad7a-1993b0113472 | -7.17249 | -43.71091 | 2026-10-07 16:37:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c9b9dffa-20bf-304d-a498-342b02b1fbd5 | -6.23963 | -53.46746 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8800352d-4914-3b74-8840-8ec09af1a23e | -9.86826 | -46.30994 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 257bf774-a19a-37ed-93b4-1a664eefe690 | -5.15344 | -41.16708 | 2026-10-07 16:37:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 88b81c29-f068-39d5-91e2-0fa333751a18 | -3.70626 | -40.82957 | 2026-10-07 16:37:00 | NPP-375 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 8fcd776e-405e-3ac8-b2ab-9c695141f046 | -5.49958 | -42.84431 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| e2ccda84-20f1-35ff-b21c-12c79ba8c0e6 | -3.95539 | -41.53828 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 23.8 |
| e0ef3eb6-d318-3260-bc8f-7ad74f89d78c | -3.81239 | -41.69828 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| f6fed86d-3ddd-372c-a2ef-95a0e4ba265d | -7.12575 | -43.91086 | 2026-10-07 16:37:00 | NPP-375 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c1b68d06-cc1f-399d-a967-55a52d315f34 | -7.40045 | -38.85274 | 2026-10-07 16:37:00 | NPP-375 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 062bab6a-b847-3973-97a1-b5e28a333968 | -8.95731 | -47.58147 | 2026-10-07 16:37:00 | NPP-375 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ea3b8100-2366-3342-9edc-073fc3f9a9b1 | -11.06598 | -45.77291 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6a458cd1-4a4a-3dbe-b28a-489fe2da3ad9 | -5.96633 | -43.87095 | 2026-10-07 16:37:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 238c9106-5c0c-3840-a542-e212a2d44ac1 | -5.97151 | -40.91674 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 290.5 |
| 291887ee-5325-31ef-a889-8054d1912c00 | -5.95463 | -46.37508 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| fcee387a-cb7f-3364-9090-afe34bdf822a | -9.82952 | -38.37697 | 2026-10-07 16:37:00 | NPP-375 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 914d80e9-bbdc-3700-9a49-f6c6d5abf263 | -8.25919 | -54.70881 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7321e6be-0e29-3b94-be68-431a55a16d96 | -5.95277 | -55.34141 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| fb95129c-d7ae-38dc-8bff-520b7d85479b | -10.88067 | -46.67451 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 3d1b019b-ff5a-3fe9-87b6-afb23ef876de | -11.00005 | -45.46953 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 137a7eb2-9140-3100-bd4e-3bec5c8d0949 | -11.05759 | -45.86515 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| e4140df5-dbaa-3a81-8a83-067ba1f108f1 | -6.18813 | -52.83411 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39272f7a-5d24-3731-a378-18b8762acf90 | -7.86991 | -54.97155 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| a7e4b481-3794-3a70-8d0c-7dce249c048e | -3.8097 | -45.40062 | 2026-10-07 16:37:00 | NPP-375 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f985a836-ce1c-34b2-a5fb-7eedabdc301e | -5.97028 | -40.95586 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 26.2 |
| f9755a72-29f7-31ee-976b-35669823bcbe | -7.1672 | -43.76501 | 2026-10-07 16:37:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dc06a524-4870-3144-99ee-cca6b2c8140c | -7.54237 | -37.36906 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 7.4 |
| cb744535-10eb-32a4-92ab-d1c6ebe7839c | -11.09314 | -45.66697 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 25b482a1-3ff9-3414-aca8-bec7266f9321 | -17.24734 | -44.42914 | 2026-10-07 16:37:00 | NPP-375 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 71caea98-b7b1-32ba-bde2-0aaa5f1ad10e | -5.97159 | -43.29459 | 2026-10-07 16:37:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8cefc55a-6a03-33b4-b1a1-e497941e6471 | -15.63643 | -43.29264 | 2026-10-07 16:37:00 | NPP-375 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 04787204-0122-3b7c-a96c-1ccc9a105fe0 | -8.76513 | -44.15713 | 2026-10-07 16:37:00 | NPP-375 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 82d50182-8710-3092-9e96-f69d9a329eed | -6.97958 | -45.12775 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e46a0061-0a8a-3cca-a02c-edc2d0a45827 | -7.56214 | -47.78274 | 2026-10-07 16:37:00 | NPP-375 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 6cd0d03f-aa96-351e-8251-fcbe7917a63f | -3.50547 | -41.94796 | 2026-10-07 16:37:00 | NPP-375 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 8a121a27-c375-3e25-b4c4-f816dd48718e | -4.84565 | -40.39148 | 2026-10-07 16:37:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 11.4 |
| de4521e3-1ca6-3623-a7d8-28273b604216 | -3.31477 | -43.27359 | 2026-10-07 16:37:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cc54e494-8137-34a2-ae17-b9b761f4a003 | -7.69675 | -44.73954 | 2026-10-07 16:37:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1ecc899b-e22f-3e69-8d8c-c99ac496e5c9 | -4.66392 | -40.56437 | 2026-10-07 16:37:00 | NPP-375 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 73f0af75-9264-3943-b05b-d17e6c9b5f81 | -3.58471 | -39.44922 | 2026-10-07 16:37:00 | NPP-375 | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8a85d257-5593-308d-9954-ac7a4c0efc30 | -8.07132 | -45.59419 | 2026-10-07 16:37:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7b1058cf-6ab1-3ca8-8de5-5fda61448f80 | -5.50354 | -42.82524 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 800c5cdb-94d4-3204-b93c-02402aca4c8c | -9.38248 | -45.92154 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c2e0d09b-a6ed-30c4-a18a-a314ae5b8979 | -3.8632 | -43.02749 | 2026-10-07 16:37:00 | NPP-375 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| bf3c2d61-ef50-340e-8692-4cf6d24ed9e6 | -4.17358 | -42.04528 | 2026-10-07 16:37:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 3142a2b3-ee9f-3530-a61d-fddf27423539 | -3.89826 | -44.09714 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e8b5cd32-4f39-39f5-af84-1fcd97cb3947 | -6.31882 | -43.35046 | 2026-10-07 16:37:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 19b58396-f7fc-3630-be24-ade80c99be73 | -10.29186 | -47.9914 | 2026-10-07 16:37:00 | NPP-375 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1f820c3b-db6f-3a17-bf87-e092dd85beff | -6.20897 | -52.79305 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 35ace34d-053e-371d-b32f-674348ac3f58 | -4.12156 | -41.78508 | 2026-10-07 16:37:00 | NPP-375 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 9e5a51f3-4966-32aa-9f1e-e28ea2afcc56 | -16.12705 | -43.74436 | 2026-10-07 16:37:00 | NPP-375 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 805cddb0-da83-3041-910e-f432154d6273 | -5.85474 | -42.65814 | 2026-10-07 16:37:00 | NPP-375 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| c21bf29e-0917-37b1-9705-8102dc348835 | -5.28106 | -50.0939 | 2026-10-07 16:37:00 | NPP-375 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b5638ec5-87e4-3bf7-937f-699ce4ac2b5a | -11.10663 | -47.58121 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0a02d397-52de-34ea-b512-90f8f9ccf7af | -10.45825 | -46.83969 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 5cc4f513-7778-35d8-8f0c-7430df845e37 | -4.58183 | -40.7707 | 2026-10-07 16:37:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 4f7348dd-0a2d-313a-9a2c-7c2c1dfceabb | -7.12588 | -44.06723 | 2026-10-07 16:37:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b107dba1-2d09-3b45-8cff-d1351a2ca503 | -6.64589 | -43.78098 | 2026-10-07 16:37:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 76581ae2-5329-3474-bee4-73d32b6c4397 | -5.89438 | -53.63897 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 5d64b005-dbd3-3687-ae6a-15269303819b | -6.01469 | -53.50117 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 806c3781-0472-346f-bb2b-26f1aadac9aa | -6.80671 | -55.29926 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 600277c8-965e-3b1e-ad2c-ddac9db739b4 | -6.03489 | -43.02703 | 2026-10-07 16:37:00 | NPP-375 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7159fa6-3590-3f41-8b50-cf096721f52f | -6.82287 | -38.53415 | 2026-10-07 16:37:00 | NPP-375 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 41.3 |
| 62fbee0d-d59f-3388-b773-95146270465f | -6.68324 | -45.334 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 73397a3e-35d2-37d6-8ca4-5874e0e858ef | -10.89646 | -46.66453 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2b601847-78d7-3f0b-88e6-c210efc21a0e | -4.80109 | -42.75283 | 2026-10-07 16:37:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c102411b-b853-3b21-bdb6-ef4fcb235cb0 | -14.7526 | -41.82479 | 2026-10-07 16:37:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 299ffe03-6f8b-3780-a61e-78f523dd2c40 | -6.38524 | -42.54429 | 2026-10-07 16:37:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 767c8dad-1d13-3853-b3db-be837fd96418 | -7.29798 | -48.62266 | 2026-10-07 16:37:00 | NPP-375 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a80af20a-d609-3a31-9c42-2784bcbe732e | -8.96736 | -47.57038 | 2026-10-07 16:37:00 | NPP-375 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 311901e3-ac6f-328f-9e7f-070aa414c3f1 | -5.88197 | -51.19605 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6d60c9cc-39a4-3493-b23e-aadb1922854c | -6.2229 | -52.85504 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| e08c8bca-414b-30fd-ba44-33de0752749c | -5.13028 | -42.77987 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c8f5818c-c0f0-34d3-87c6-620b2732fe2e | -6.94227 | -45.2685 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0b7b73cf-2d41-3327-97e7-072a7477f18d | -9.71119 | -35.9301 | 2026-10-07 16:37:00 | NPP-375 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| d86f1bc6-accd-3709-b2e3-7a8811ed0180 | -5.48088 | -45.63686 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 93dff3e0-0b61-351f-972e-7b49f924ee9c | -7.16441 | -43.769 | 2026-10-07 16:37:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4dc2419b-cb43-3596-8b14-15015797439b | -6.23373 | -46.00694 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a2666ba2-95c7-3504-94fc-b8330b66d3dd | -6.80606 | -55.29446 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| a2ef024a-a330-371b-a6e1-4a41c3c44abe | -6.8612 | -41.79838 | 2026-10-07 16:37:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 226f7ac5-65b5-3529-8b48-47a866b7e537 | -9.93654 | -46.80017 | 2026-10-07 16:37:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a59449f8-be8a-3d96-8fa5-2f6a383021c0 | -5.72066 | -41.7474 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |


[Clique aqui para ver as próximas entradas](README216.md)
