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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e82f84e5-3148-350b-a1ac-9705835dac3a | -21.53448 | -46.76431 | 2026-08-16 03:40:00 | NPP-375D | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| cb6e175e-5e45-3b1b-9d7a-5294b0ff7176 | -21.5285 | -46.76173 | 2026-08-16 03:40:00 | NPP-375D | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 8ad7adbc-7443-3073-ada4-e77996425520 | -8.9415 | -60.5174 | 2026-08-16 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 2d92e8f3-9b5e-33e2-aa9d-f4f9c85a2707 | -6.6194 | -59.0609 | 2026-08-16 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| d5356005-4aea-375a-9a76-4907bb401ef4 | -6.1108 | -57.7035 | 2026-08-16 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 96861f24-572f-3d36-80be-ba1aa7539635 | -2.9623 | -49.2587 | 2026-08-16 03:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 5b8f0ee1-0fdb-3d9c-b889-68e6719f2d7e | -6.7123 | -58.9412 | 2026-08-16 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 008c6894-1df5-31c3-ba02-f796eaef464a | -6.82 | -56.4551 | 2026-08-16 03:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 02d2d101-d5e2-312f-b6b2-a97403c0326b | -8.9601 | -60.5165 | 2026-08-16 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 167.0 |
| cc8caabb-132c-390c-9ae8-dfe68003351d | -8.9785 | -60.5349 | 2026-08-16 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| bfef3ef5-92c6-33a2-a129-57cb5f88f6b3 | -6.8597 | -58.9738 | 2026-08-16 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 88705dcd-d50d-3383-8c70-05a98fa3c958 | -6.6377 | -59.0795 | 2026-08-16 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 244bcbfc-16ac-3868-becb-932a6771aed6 | -8.9787 | -60.5156 | 2026-08-16 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 0b502c76-0a3a-3382-98ce-ae532bdb33fa | -6.8387 | -56.4344 | 2026-08-16 03:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 10f99425-3c16-3180-9c2c-210b1826bce9 | -8.4275 | -62.676 | 2026-08-16 03:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 9e83fcc3-a444-3bc0-a1d2-fadb2d14c4ad | -6.6938 | -58.942 | 2026-08-16 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 1ffb573b-262a-30fe-b768-5fdb7eb87fa0 | -8.96 | -60.5358 | 2026-08-16 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 149.7 |
| a52ea797-56a9-39b4-9c0c-205e083e83e4 | -6.6193 | -59.0802 | 2026-08-16 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 60f7c657-e244-3ca6-bae0-289867f2df7c | -2.42859 | -47.03442 | 2026-08-16 03:51:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9895178-ad6e-3086-82b9-bbfe6f612f2d | -2.90659 | -40.4393 | 2026-08-16 03:51:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 15271ca4-ba01-3354-8afc-9888687265ca | -2.43463 | -47.03531 | 2026-08-16 03:51:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c00439a-42dc-3865-8943-d2f6af1ffd94 | -2.43075 | -47.03219 | 2026-08-16 03:51:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 08ed7aa4-a75f-3aa8-9b37-a3a545fd8a35 | -6.43609 | -37.08917 | 2026-08-16 03:53:00 | NOAA-20 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| aa99a644-3f06-3a8b-bdfb-0ef4bb8e052c | -7.25444 | -44.69289 | 2026-08-16 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed57d309-6d72-35a9-b4d8-4f54ce16b271 | -6.20778 | -47.73101 | 2026-08-16 03:53:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| dd39aebc-0f4a-3f44-966e-153432342609 | -6.23146 | -47.73528 | 2026-08-16 03:53:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4640ff87-18ff-3afd-b4cd-b379d679f960 | -7.25938 | -44.69489 | 2026-08-16 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5aef502d-0a51-31dc-b1aa-53bcf93f3fc0 | -6.29055 | -47.74669 | 2026-08-16 03:53:00 | NOAA-20 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9046a662-6e7b-3814-b3ca-7cf7763ab4a3 | -6.05403 | -44.88802 | 2026-08-16 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6ad72ff-7c49-37e8-a5d8-176993f4e84c | -7.20431 | -43.15829 | 2026-08-16 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9ccaf23b-fd6e-34b8-964e-383b12cef3f2 | -3.49736 | -48.04244 | 2026-08-16 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 833848bd-1deb-3ba3-90ff-06576ae19035 | -7.22255 | -43.16839 | 2026-08-16 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e2f8b362-d0d4-3c57-8f78-639c5dc5a792 | -7.6455 | -42.75703 | 2026-08-16 03:53:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3bb0fb7d-7cd9-38ff-b892-e36f92862f2c | -4.10085 | -42.50048 | 2026-08-16 03:53:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 452c5bb5-2756-3ef2-b0fe-0b92c6fc65b8 | -6.2129 | -47.73649 | 2026-08-16 03:53:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 052ecd64-30a1-3d5e-9d8a-daf8d56f9eba | -7.81293 | -44.10476 | 2026-08-16 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aca132d4-8e8c-3319-a4ef-c0326bc8fb1c | -7.5829 | -45.03573 | 2026-08-16 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d976c11f-fb99-39ec-9d9e-9ddb9bad3dee | -6.28976 | -47.75114 | 2026-08-16 03:53:00 | NOAA-20 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ea7fd717-5bc1-397f-a209-d8c6c3a47ce9 | -7.27947 | -44.71991 | 2026-08-16 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58f4ee7f-cf31-30a9-adfc-e260ca496ea9 | -7.99185 | -38.32941 | 2026-08-16 03:53:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ed452a21-f792-39b8-8cdc-36707d421e98 | -7.36657 | -46.84975 | 2026-08-16 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 042817ec-44bd-364e-86ce-ab223cc5426b | -8.79781 | -45.79235 | 2026-08-16 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b9d885e-03cb-3afe-8828-2bb64f088ba1 | -6.9126 | -43.63255 | 2026-08-16 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 155220d9-7c03-301a-92c5-ffd824a08bea | -6.67677 | -43.99811 | 2026-08-16 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4d375d41-fa93-3dc5-a8f4-e1e74ed1b12f | -6.9953 | -45.91079 | 2026-08-16 03:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 537585e6-7c6f-3568-b76e-38e97e73757f | -6.28695 | -47.73252 | 2026-08-16 03:53:00 | NOAA-20 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f48408d-f173-3c1b-8ae7-828e7c2d5c42 | -7.25369 | -44.69924 | 2026-08-16 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9eaecb17-c208-3a0e-a09d-2d0f47032e0c | -7.00055 | -45.91135 | 2026-08-16 03:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d674ddbe-2444-34dc-8ac0-33338b437318 | -6.67305 | -43.99237 | 2026-08-16 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5ffddbd6-4267-36ad-81b7-6bc887afd2f3 | -6.67221 | -43.99719 | 2026-08-16 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8ad6a7f2-9d8a-3fff-9e78-9b5ae5c7885c | -6.29422 | -47.74646 | 2026-08-16 03:53:00 | NOAA-20 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 64715e24-4d5b-3925-9afb-713bae8bc9e3 | -6.88435 | -41.95781 | 2026-08-16 03:53:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| affe60a6-c470-3864-bcaf-6c495c6f3812 | -4.10379 | -42.50945 | 2026-08-16 03:53:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a00afaa3-297b-390f-b990-95e99dd63b51 | -6.986 | -45.90285 | 2026-08-16 03:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75695aa5-4179-3678-83e2-1bd32258f95b | -5.2574 | -47.7093 | 2026-08-16 03:53:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cfb08b7e-b6a2-3794-ba54-2388b8b6670d | -6.88152 | -44.97575 | 2026-08-16 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dcd9ad0b-1fbf-3465-8c94-8e23e83830a5 | -6.91507 | -43.6343 | 2026-08-16 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79b7154c-b5c9-376a-9ae0-a20b630d6f01 | -6.9739 | -41.29322 | 2026-08-16 03:53:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 136bd354-4663-3b1a-802b-94d63b771a78 | -9.06238 | -45.78319 | 2026-08-16 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e43ee7c7-0a04-3474-9e91-28adcb645c34 | -6.96021 | -44.23759 | 2026-08-16 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 546569b6-73bc-3e90-a788-f04b59dd3dfb | -2.82362 | -46.73379 | 2026-08-16 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 673ba17a-5e0d-3aff-8879-dc7e3c42c5b4 | -6.28617 | -47.73688 | 2026-08-16 03:53:00 | NOAA-20 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48f3acbc-91d7-32e4-a2fe-c2de16605872 | -6.28743 | -47.7501 | 2026-08-16 03:53:00 | NOAA-20 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eeb7394c-3117-35ac-9d00-369650e0c0fb | -7.81749 | -44.10537 | 2026-08-16 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c33bf011-e563-3fea-b790-5b22e4fef406 | -4.09722 | -42.49563 | 2026-08-16 03:53:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3b9e48b9-137d-3bfd-b8f1-8aec7d224296 | -2.76595 | -48.56958 | 2026-08-16 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0e332109-6e8e-375f-915c-133b61fc3187 | -5.69847 | -36.25333 | 2026-08-16 03:53:00 | NOAA-20 | LAJES | RIO GRANDE DO NORTE | Brasil | 2406700 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c36e1d32-4bb8-369b-9965-9586b54ca6e4 | -8.4023 | -48.48729 | 2026-08-16 03:53:00 | NOAA-20 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 483243ef-1a2b-3767-be0f-02ac498d653e | -4.09653 | -42.49976 | 2026-08-16 03:53:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 551a0c58-c64c-3bbc-8bf3-062c0c9867aa | -7.20323 | -43.15249 | 2026-08-16 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2d8cb3b7-9446-3e46-a033-9929cb9df4df | -7.25831 | -44.69893 | 2026-08-16 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b5a27f76-c994-39e9-ae2e-2657945b832d | -7.27563 | -44.7139 | 2026-08-16 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cee692d-c8cc-31c7-b471-8003c89b5bbf | -6.30462 | -43.6164 | 2026-08-16 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 43b1f04a-e4fd-3c90-b804-fee20a58feda | -6.99737 | -41.43404 | 2026-08-16 03:53:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c2f659dd-313b-377c-9f28-098d5b50ef12 | -7.27471 | -44.71903 | 2026-08-16 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fe4646da-da3c-3097-b034-e14cf7a89e14 | -6.05501 | -44.88248 | 2026-08-16 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97b31fdf-c6fa-3d4a-92cc-c3f4c6be2538 | -4.11017 | -42.4978 | 2026-08-16 03:53:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d1479180-faef-3e97-8855-4d055fa4276e | -6.23735 | -47.73653 | 2026-08-16 03:53:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4954cde9-a41c-3fd8-bf66-3131bd832994 | -6.86251 | -43.87505 | 2026-08-16 03:53:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b428d47-ed4a-34e2-af88-a05425a66c4d | -8.35058 | -45.98252 | 2026-08-16 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9f4dab14-9c5c-3ce9-9216-7302a9d8250c | -2.82243 | -46.733 | 2026-08-16 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01a3360f-6f4f-3188-b990-e8bf8aec5b94 | -8.79839 | -45.78921 | 2026-08-16 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba36315d-8853-3b7d-8609-f56fc6c00baf | -6.93211 | -43.64183 | 2026-08-16 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd0f02c2-83da-36f8-bc8b-3e4d13636db2 | -6.28477 | -47.7314 | 2026-08-16 03:53:00 | NOAA-20 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b667c12-7266-3f67-af5f-1682df1762de | -7.22398 | -43.16021 | 2026-08-16 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4561c939-a70e-363c-8b7a-bcb43777ed1f | -9.05742 | -45.78226 | 2026-08-16 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e68fc8e3-fbf1-3cfb-802e-f0b5d2c50baf | -6.92399 | -43.63578 | 2026-08-16 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 29128916-de04-363a-98ff-457fb991357a | -4.10517 | -42.50121 | 2026-08-16 03:53:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2ac427bc-87c1-3a20-8f45-303ad0019b2e | -8.94807 | -38.00094 | 2026-08-16 03:53:00 | NOAA-20 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 82d916e2-7aa4-39bd-be92-e99c2f12e950 | -6.55752 | -43.11205 | 2026-08-16 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc7251bf-d810-3b9d-8557-e03d6e9ec906 | -6.05773 | -44.88746 | 2026-08-16 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f13d34c1-b56d-3527-aafe-48c2f205fa51 | -7.00968 | -41.43147 | 2026-08-16 03:53:00 | NOAA-20 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5ff5279b-cc68-3c56-b629-0eaa6df35f02 | -7.20251 | -43.15659 | 2026-08-16 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1841cdd6-915a-3696-84ac-7865c56d488c | -6.99473 | -45.91396 | 2026-08-16 03:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e208de5d-372b-386d-8e5b-6a7cbf962182 | -6.8775 | -44.96989 | 2026-08-16 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 640e1802-c1bc-39e9-9a77-c7f3862d2d9d | -5.63225 | -44.11459 | 2026-08-16 03:53:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9e09455-4120-36e1-b4db-1810a244e437 | -6.30988 | -43.6127 | 2026-08-16 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec7dd0bd-64dc-3824-b463-cce7790fb131 | -6.21962 | -47.73314 | 2026-08-16 03:53:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f124603c-60d4-30b6-a53d-005182750c53 | -8.40315 | -48.48286 | 2026-08-16 03:53:00 | NOAA-20 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 23853f88-9023-34c9-b2d1-25b4ef6d2529 | -2.82292 | -46.73805 | 2026-08-16 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README10.md)
