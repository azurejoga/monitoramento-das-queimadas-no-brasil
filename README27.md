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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ba0429d-4cec-341d-ab13-e6e7e24fe183 | -10.01164 | -46.39312 | 2026-08-31 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8924bcc0-eda0-3518-adbc-19cb647d969e | -7.41288 | -44.25017 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1792f9d1-5f44-378c-9283-3b66b95bd7dc | -6.48411 | -49.89752 | 2026-08-31 04:14:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0284cdb7-daee-34a3-9180-a92e64359313 | -7.9095 | -44.27727 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da9367b3-32f6-32d7-8fae-b19842334b12 | -11.35335 | -45.22406 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d37cade-d8e5-3e13-a6c9-7319d2b2bc1d | -10.75074 | -44.88039 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 035b6ea3-11f1-3b03-a077-3faad5680cf6 | -12.92448 | -41.77976 | 2026-08-31 04:14:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 00cec5b9-2d87-311e-a468-6a297f317c88 | -11.21253 | -45.34993 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72d432b9-928d-348c-8525-9a2dd5bb5d93 | -11.34552 | -45.20685 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ef6d5618-4972-33b2-b4f6-b5b0b5fd36ba | -11.35182 | -45.21193 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b26fb896-0e91-3eca-8172-222fbe10c417 | -6.37822 | -45.46352 | 2026-08-31 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 16d94411-2ea4-3841-8810-d9b0e58d7ab6 | -10.14489 | -45.68614 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 847ff859-2f01-341d-9174-e72afbfe2bcf | -11.68563 | -47.6029 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 74b12b4c-dfd7-328c-8fe8-d6ef61e632d7 | -10.1466 | -45.76537 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| feb3cdef-a0cb-320f-96c3-5cefa38e2883 | -10.73471 | -47.95892 | 2026-08-31 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c2afc47-7505-37f0-9084-910d6f004d68 | -11.92992 | -45.05059 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5692911-795c-3a59-8cf6-5713ab9c3f1a | -6.77261 | -55.6424 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| ddef6fcd-4d52-365c-9278-b80440a4b4ed | -12.39488 | -46.44837 | 2026-08-31 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 332ed8b9-4296-3526-aea3-5a82d14c0bb5 | -7.52858 | -55.33887 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 777e2731-dff8-3a1c-8f2f-3f0b3c4eee43 | -10.15 | -45.69987 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af4efb68-2d17-395b-a241-019c3fc8433f | -10.8541 | -50.48962 | 2026-08-31 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1b89a7a-0a8f-3eaf-ac61-10bd59d9bd72 | -7.10696 | -42.18372 | 2026-08-31 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6dbd2e53-09a5-3056-b311-d01a541f816e | -8.75104 | -46.45378 | 2026-08-31 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 77abcf78-0004-3d48-ba5d-f77d57f117f7 | -7.95058 | -44.26479 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1900073e-c076-3cf8-96b0-d0740eeb5d2b | -10.73349 | -44.8775 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6dd6a783-8074-39c1-aaca-15f623cabb87 | -7.54762 | -47.3271 | 2026-08-31 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e645f4c8-1f0c-3b73-a8de-8e2e6c0026e1 | -6.93513 | -55.64014 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ba5b9464-8562-3512-904b-c0ff49f68580 | -5.4565 | -42.64439 | 2026-08-31 04:14:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8e1ab2f2-825d-3c56-9d24-65e6e6546413 | -10.15761 | -45.73012 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 19a94734-3289-38fd-820e-495201bfc366 | -11.33175 | -45.19314 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc018e5d-66ba-3575-8b32-7d60537bac9d | -11.47727 | -45.06967 | 2026-08-31 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 450996ca-fbb5-3f58-94a8-033e75447250 | -10.15665 | -45.72678 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4923713-3f4d-31d4-bd4f-cf349bbe9b06 | -12.14445 | -47.25508 | 2026-08-31 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76db81ba-f574-3550-85b8-65bcdd808bee | -6.9323 | -55.63318 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8d87331f-1feb-3ed1-b351-f77513f3ce02 | -12.12245 | -45.03201 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e63b44c0-f79c-347f-b9d6-5b2059f1eede | -7.36846 | -45.06973 | 2026-08-31 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bca95831-c125-391b-af50-4ed68035306b | -10.84702 | -45.36425 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01d1d594-1084-399d-b51a-45a2b9546e52 | -11.21106 | -45.11448 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a99a638f-24b4-37b2-a063-d44b24b777f3 | -11.21835 | -45.09181 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f4026b31-04cd-3c4a-b546-10e67726b669 | -12.11603 | -45.0315 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9877894d-0d77-35bb-877c-64229b5c2f56 | -6.78806 | -42.75568 | 2026-08-31 04:14:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8f75d058-da2f-3d28-a686-1e2e3978c139 | -7.09653 | -42.84457 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5fcfcb40-f447-3c7d-8504-cac1e6e0cc32 | -8.33203 | -45.65313 | 2026-08-31 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 082cfdd4-7ff8-3d4b-bb20-710c49d4f6be | -7.34419 | -55.18516 | 2026-08-31 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3061777e-604f-35c1-a6cc-e0774cc4800e | -7.77737 | -44.05839 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f4319cd-8278-3425-8693-7c8f987e2d69 | -11.33521 | -45.19375 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a42837d8-79bc-3f6a-aadf-a66a9ac96990 | -6.86415 | -44.43517 | 2026-08-31 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e69fe0cc-fdb4-3ad1-a199-fe344e8ca46e | -10.14876 | -45.76018 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 94b3e662-8dea-394e-bebe-a7fff3342f97 | -11.32481 | -45.19188 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8b6c53d7-803b-328f-aba7-86127a18b9d3 | -8.74419 | -46.44792 | 2026-08-31 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26b838e6-a163-3c68-b1cb-8d38884e4e10 | -11.22265 | -45.15236 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7393f6a0-89f8-3509-93d7-632cd2a6358a | -9.97238 | -46.765 | 2026-08-31 04:14:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b70b6c5f-b932-3e7b-9ed0-bd43527c6f3d | -6.27694 | -53.33244 | 2026-08-31 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 261565fe-4270-3940-bef0-9403f7063f5e | -11.60633 | -46.7215 | 2026-08-31 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d73a9b4b-97bd-3af8-9274-2572a5d87787 | -7.41728 | -44.26692 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa80c370-82a0-30b6-8edf-af2aea247271 | -7.09042 | -42.83997 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 15b29ea1-99fd-345a-817a-a1032ed04e85 | -6.91771 | -55.72895 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| cfb65c8c-ad9d-30fd-9fc7-3c77ef440b64 | -10.99334 | -49.68904 | 2026-08-31 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcf410ae-8bd3-3965-8b92-f310430ed486 | -12.3985 | -46.44906 | 2026-08-31 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1edd3198-001a-38fc-bace-b716d2db2754 | -10.12685 | -45.70581 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ead10aed-6a43-3b72-a4a5-5f0a5eb82c8c | -7.12866 | -44.30822 | 2026-08-31 04:14:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8eb92b4-eaf2-396a-b8b3-cc4a8e6ecd56 | -5.58612 | -42.3261 | 2026-08-31 04:14:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bba7267d-420d-3792-9ea7-f39b1d4fe398 | -12.0778 | -44.98558 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9aecdc1c-6337-374a-a7af-7d597f032db0 | -7.14268 | -46.1712 | 2026-08-31 04:14:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d63b3491-3fa9-3bf6-bd07-6b8b60fe1ae9 | -12.09358 | -47.18707 | 2026-08-31 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 212bd42a-5120-3c13-a701-f7f67dc6b80c | -5.60481 | -44.00265 | 2026-08-31 04:14:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 72e6d427-512c-309f-9bb9-97d39920ff73 | -12.41674 | -42.88627 | 2026-08-31 04:14:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 88d22eed-52f1-3be1-90de-7b9431eb65de | -12.13487 | -45.83889 | 2026-08-31 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aedf924d-db1a-3349-832c-1426168639c4 | -9.18747 | -51.55193 | 2026-08-31 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4b9f540e-9132-3b2c-8f5c-2ea7f6dcaff4 | -7.92144 | -44.29096 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d026e98-0a07-308a-ba23-d66ccb7140a9 | -12.08062 | -44.9898 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7f4b540a-0a4d-34e9-b190-e8c4f746af09 | -7.13122 | -44.30577 | 2026-08-31 04:14:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d4c2f47-a72d-3410-beb7-f5f5f38ecb2b | -7.18891 | -46.57095 | 2026-08-31 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83903071-f550-355d-b595-1e13928da56d | -11.36611 | -45.1905 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4160d1ca-e621-34a8-8815-a6d67add033b | -11.34746 | -45.19532 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12fdaa16-f4cd-3a38-8b28-baa1f1bb8426 | -6.27606 | -53.33725 | 2026-08-31 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c57c2ef5-d098-3947-8b35-685354008ae5 | -8.0819 | -45.4689 | 2026-08-31 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a80d04d-cb8f-3f42-8555-2d6f190c8139 | -6.93806 | -55.64136 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4a31a7c1-6a87-318e-82d2-0c4c6a1b9be4 | -11.53792 | -45.48533 | 2026-08-31 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2223b5c6-e63c-389a-b39f-4d7bd8a05f6f | -7.04461 | -42.19156 | 2026-08-31 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4fafdb72-8a41-3fe4-ba83-2ba05a5258dd | -6.43527 | -41.53435 | 2026-08-31 04:14:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b978ef6e-2cd8-302d-b3ca-612ca8825066 | -11.79056 | -47.66916 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e83ebc9-d3a0-3ddc-8599-e463622c35d0 | -7.92082 | -44.29476 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a9fb147-06ca-3814-b7ee-68d6c8e44dca | -7.6121 | -44.84596 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3cfcc5b-451f-36e6-823b-ef801fdb22dd | -12.13338 | -47.22835 | 2026-08-31 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b30234be-8175-3e03-b58c-9d3b9cd99b2d | -10.05534 | -48.69408 | 2026-08-31 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d4df7c06-8b4f-32ba-b48d-c3a9181142a3 | -11.36506 | -45.21818 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4efecb5a-be3d-3059-8c14-016cfba1c3a4 | -7.18456 | -43.71255 | 2026-08-31 04:14:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de3e77d4-c38f-3670-8a2b-72405f8d92fe | -6.95121 | -55.7079 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1d99f5ba-34a4-3697-9aff-27ed8ec466e5 | -7.14426 | -46.17363 | 2026-08-31 04:14:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db721d0a-1f62-3a38-8e57-f7c8348af9b2 | -6.8722 | -41.69217 | 2026-08-31 04:14:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1735d016-0471-3b47-8528-961641c5d020 | -10.15179 | -45.74248 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8b26024c-7abe-31f5-b4f6-57cfd42e0a62 | -10.84417 | -45.35966 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26b97caa-e6bf-3b62-b863-0eaf22e86700 | -11.33049 | -45.20074 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b1fe4b7-4345-332e-a919-293b702c927b | -5.60831 | -44.00319 | 2026-08-31 04:14:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ce392a58-5463-3ff4-ad45-3dc3dcd5e682 | -7.62423 | -44.92728 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ffd7537-e78d-31eb-bbb5-2e29d51ac606 | -6.86765 | -44.43579 | 2026-08-31 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e4aa8eda-43e0-32e0-b494-16c5f8492dfa | -9.42406 | -45.6509 | 2026-08-31 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f651d283-7a29-3aa6-bcdf-8c9bee97faab | -11.67606 | -47.61169 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| de25d4f9-6e9c-3f06-ae44-bf46b2fa17f2 | -11.7954 | -47.66472 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README28.md)
