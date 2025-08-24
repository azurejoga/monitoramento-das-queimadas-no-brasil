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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21e45437-d15f-3c74-8f5f-dc55f9745d8b | -7.81306 | -46.62595 | 2025-08-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 71734e09-83c5-350a-b3ad-81719e3faf86 | -5.60915 | -60.2376 | 2025-08-24 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 009e8833-c603-3c8b-9592-ec84ec69c6ec | -8.5384 | -48.86148 | 2025-08-24 04:34:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96048682-714c-3e04-b785-6aae79259fcb | -8.53785 | -48.86496 | 2025-08-24 04:34:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08e9725b-65c6-39d1-b0f5-86592e4d84c1 | -8.0652 | -49.65426 | 2025-08-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f281c29-fb80-3694-a3fa-56a8e7c4c1db | -7.03292 | -44.66076 | 2025-08-24 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7ecb8d9a-27e1-3861-ac3b-8e5f7888b9e0 | -7.70215 | -42.1317 | 2025-08-24 04:34:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 20155487-fb5e-33c3-bd35-387294d04f86 | -9.5706 | -47.95377 | 2025-08-24 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ab41bf61-3f10-3569-98d2-25480ba060e4 | -13.49683 | -47.02857 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edac0d15-cb24-3a05-8aed-015c56d36b7f | -13.05294 | -46.31926 | 2025-08-24 04:34:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c389cb60-dc2e-35a3-a2fc-2e251ddddcc3 | -6.96142 | -44.17727 | 2025-08-24 04:34:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f3f3458-5df2-3ac0-88d2-5ee473037c6b | -13.47973 | -47.02286 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| da5851a0-deea-3722-9c77-ab85655885f6 | -8.20619 | -44.42514 | 2025-08-24 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba8b6880-a498-34be-8ff7-efc3c3ea6aa2 | -9.13608 | -60.784 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6de35118-8539-3739-af33-9a956b89c811 | -10.25299 | -49.09774 | 2025-08-24 04:34:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc90c929-0a0c-319c-afc0-d2988c4fbe38 | -11.52429 | -50.4929 | 2025-08-24 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 088df930-8bec-379a-8a92-32c89092d7dd | -13.05168 | -45.22831 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ae32c68c-7654-3fb7-a9ff-9de3384a7bdb | -9.02263 | -59.01544 | 2025-08-24 04:34:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53b902db-10dc-34c8-ac0c-71f705223b27 | -10.76009 | -48.26395 | 2025-08-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b57cf0d-f8bc-39ab-97c9-b2ef23e3cdec | -13.41267 | -51.81589 | 2025-08-24 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e40fcdc-1211-3559-9c95-3f4730af2f9b | -10.81231 | -46.41825 | 2025-08-24 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 765d5f08-a397-3826-88be-db870fc83a6d | -11.13651 | -46.32951 | 2025-08-24 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8bdf08aa-4f9d-3b7f-84f4-8ad4b166d7ed | -8.19007 | -45.08035 | 2025-08-24 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85338d69-1398-3a27-96cb-081f83e3e0d4 | -7.17084 | -44.66539 | 2025-08-24 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcb606ae-2ecc-3357-ba52-a4e5df6f5f40 | -6.68169 | -58.85346 | 2025-08-24 04:34:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9c908c6c-cd0d-3a47-be78-26858e47a082 | -13.04648 | -45.23745 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3c5c1959-4e35-3e5e-8152-bcae50425803 | -7.59683 | -45.24592 | 2025-08-24 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b93502d1-6f05-3792-8cae-04ccefaf2b0e | -8.61105 | -62.59632 | 2025-08-24 04:34:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 321ebf87-e421-3057-872b-cf799a3e2660 | -9.15132 | -59.45078 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 56d4ae5d-dc48-325e-a920-038c809dc3f1 | -5.42122 | -60.16881 | 2025-08-24 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6f950407-5c40-3595-9c50-c19c11e1bf08 | -9.16815 | -59.45823 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4920e33d-9401-32ee-810a-566642e9e897 | -12.72673 | -48.13525 | 2025-08-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8910e6b4-e9f2-35f3-9654-6b1ad79a4f4e | -11.61639 | -50.43387 | 2025-08-24 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5677db06-1c28-30b3-bbb3-57fa3210c0cc | -8.60393 | -62.59494 | 2025-08-24 04:34:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 53789836-cf6f-393f-a1a2-287a88a5ab53 | -7.02144 | -44.63685 | 2025-08-24 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| d10a8bd7-d07e-3caf-99e8-1f448731553e | -13.03251 | -45.22547 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a8aae0be-80c8-352f-a256-4c270476e777 | -6.26691 | -53.64632 | 2025-08-24 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bccb7d02-a2bc-311b-b7ba-b06257c25b92 | -9.1572 | -59.45183 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 70b21f40-45a7-3a5f-b53d-9933d25b6580 | -5.85684 | -52.08722 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e62b5f14-0463-3d04-870d-fb5929a4317d | -11.32468 | -47.85892 | 2025-08-24 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a61029e7-359b-3e0d-a728-7ee150bffe8b | -13.66805 | -47.98569 | 2025-08-24 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39ac3752-98b9-37e2-b886-e0745a4a411d | -5.88281 | -57.75824 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1b03b5c-3f8d-3aaa-b0a0-0d25a3751408 | -11.53647 | -51.91433 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8081ba7c-b292-3e7a-bd21-a99f5d3f857c | -8.75282 | -46.74109 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 397947fb-c0b4-3795-b944-96a00aa432ce | -8.80574 | -48.78266 | 2025-08-24 04:34:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b496860d-810f-3659-af48-27ebcc1becd5 | -7.62703 | -46.28016 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25718d85-d34a-32b9-a24a-b14934913b7d | -9.85526 | -46.70247 | 2025-08-24 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cba5570-c465-3236-916c-1953dda66d0b | -8.76532 | -46.75068 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a3edaf5-5711-3578-bdba-d80975699725 | -5.61139 | -60.22778 | 2025-08-24 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa50a2a8-d021-3f52-be9d-5b8dd118294c | -11.90508 | -47.12181 | 2025-08-24 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 732ac9d0-993a-39fb-975f-38aa5c84b90d | -5.79468 | -59.2201 | 2025-08-24 04:34:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ec67810-80b0-34b1-8edc-1b0171e670ac | -13.62355 | -48.16874 | 2025-08-24 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 046bc822-8085-3a9f-8a80-47f01e4d7269 | -8.76741 | -49.97368 | 2025-08-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c9549db-3098-3061-93bb-994fa07786c7 | -8.53952 | -37.72805 | 2025-08-24 04:34:00 | NOAA-21 | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 16275353-a690-3519-950e-8e0e8801ffec | -13.42858 | -47.04741 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76074094-d6f4-30b4-8a6f-97c3347bba07 | -8.91028 | -62.4129 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4b322494-3e90-333d-b9cb-389421133810 | -9.15856 | -59.50972 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0a12a274-f267-3bd2-976a-7cef73fab26b | -10.58069 | -47.14481 | 2025-08-24 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5200fb8a-700c-3b43-83fd-2238689f8c19 | -9.17821 | -59.46238 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0d172ea3-1617-35df-a365-74b0f592310b | -5.86065 | -52.08787 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4eb06d78-683b-3bd9-ac9c-52791dbaa814 | -9.8237 | -46.39956 | 2025-08-24 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 08358ed5-5f30-3e12-b8bc-68383808b443 | -13.35348 | -47.50823 | 2025-08-24 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29e52705-1766-3609-8916-e6f71173eb0f | -8.76232 | -49.98399 | 2025-08-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd308899-b586-38ef-9373-eeb7de296237 | -12.55408 | -45.6282 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78ea3ee1-311c-3c68-a19b-643095501fc4 | -8.30795 | -47.26044 | 2025-08-24 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b9c2b27-8169-3dc9-bd26-91eb981869f9 | -10.81 | -46.40962 | 2025-08-24 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdafc51f-673d-3324-ae2a-7692f59417bb | -11.4282 | -55.0143 | 2025-08-24 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 454ccf14-a849-37fe-ab85-e70ac14f87c9 | -11.11014 | -44.77102 | 2025-08-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11ebb381-5cda-3c3a-866e-0c4e6df96097 | -11.52823 | -50.48983 | 2025-08-24 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b2a2498-0b41-3c17-81e6-6aa69811f5e0 | -13.13704 | -44.90813 | 2025-08-24 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 204d31c2-1bfb-3e91-b726-5a9f16fddf6d | -6.95621 | -44.4215 | 2025-08-24 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b32784fd-8fcd-37ae-ae1a-c4b4d31a69f8 | -9.1958 | -59.46568 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 129715ea-0a18-34dd-a280-b2aee8b1c9dc | -7.53667 | -45.21733 | 2025-08-24 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee5db782-aaf5-39b1-8d5d-21fb037849fb | -9.19965 | -60.79633 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| be33c4e7-c679-3cfa-b521-9708dc2003fb | -6.3066 | -59.87346 | 2025-08-24 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2c960bd-9931-3e0d-b0e1-500545036964 | -9.16316 | -59.47731 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fc8e9bdc-0a58-3c30-8338-82ac65c56404 | -8.78402 | -46.74225 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1894abe0-60b7-3cfb-964e-ebfad5b5b3bc | -10.6072 | -44.32881 | 2025-08-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 373a7af2-6757-37b9-9489-689b00cbe951 | -11.52875 | -51.91719 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb4db395-e053-3f89-9a1f-ea901b78ab13 | -12.996 | -45.23492 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5190217-178a-3236-a856-a99a53e641f6 | -8.90408 | -62.41905 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6946b1c5-2f04-3204-9598-1a62888a1263 | -13.41737 | -51.80887 | 2025-08-24 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36e81956-8001-3082-80a9-db08f02f6416 | -5.10039 | -56.97809 | 2025-08-24 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 062127f4-9d5c-326a-92dc-d40a090fa228 | -9.14279 | -60.7722 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cf760ec6-13e3-3ac6-8f1c-185f2ec39551 | -8.70485 | -51.14206 | 2025-08-24 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4008bc0-8444-30c3-902f-1a36553700e6 | -11.59929 | -46.2321 | 2025-08-24 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5ea732b-035b-320b-ad54-d10eea8f90ca | -13.36708 | -46.21185 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c182c385-5bfc-3437-b393-54bdbb293fb6 | -7.91482 | -45.90389 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ec61a35-1ba4-302e-ba25-1d5168a16ed0 | -17.01457 | -47.95073 | 2025-08-24 04:36:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 838348f3-825a-3ade-ab19-a17aea2853df | -14.77235 | -55.41254 | 2025-08-24 04:36:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 060af89a-b3d3-3191-ad9a-bfab95301661 | -18.02482 | -51.08582 | 2025-08-24 04:36:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b92aceff-ebbb-337a-9988-0cd0c19a1fa3 | -18.04122 | -50.61367 | 2025-08-24 04:36:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a17d884-0884-3417-a214-c5042dcd70bb | -16.41791 | -49.14159 | 2025-08-24 04:36:00 | NOAA-21 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9876de63-7dc3-343a-bf0b-7adda6f12309 | -20.12079 | -45.36173 | 2025-08-24 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 41449a0a-6978-36d3-8069-01b14f0e5f27 | -16.07595 | -47.94071 | 2025-08-24 04:36:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ccc54b91-7f91-33ec-97e2-945c1cc8ba10 | -14.51809 | -52.04182 | 2025-08-24 04:36:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c7abaeb3-673d-378c-bb42-65210174cece | -20.59806 | -45.82002 | 2025-08-24 04:36:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e9c4c880-dc9c-3d7e-8434-88dbc6a3e85c | -17.84044 | -50.80983 | 2025-08-24 04:36:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 59eea89c-6001-37bd-8311-43c606b39fa2 | -19.61038 | -47.60629 | 2025-08-24 04:36:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2fc1a84-bc6a-3b0d-b50c-2caf17d7b8bb | -18.40512 | -46.84322 | 2025-08-24 04:36:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README46.md)
