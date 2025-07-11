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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63d6c1d0-5590-32bd-a35d-a7850b772a57 | -13.87881 | -44.45411 | 2025-07-11 04:08:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 69ca8673-9dec-3a36-9307-30fc1e60fff2 | -10.91507 | -45.11833 | 2025-07-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 86a1b16c-22e1-35d5-a6e6-a920a876e384 | -7.9468 | -49.65892 | 2025-07-11 04:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f701f99-ec29-3afd-8644-021cb7567fe0 | -13.49817 | -50.22665 | 2025-07-11 04:08:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd2c7709-1632-39b4-95e0-4dddc96c1a51 | -13.13363 | -47.30402 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4e6bc8f5-1d16-35ea-98ef-9d57961c07c9 | -8.37286 | -43.95264 | 2025-07-11 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f70055ff-fd51-343a-ae92-db35af691b0a | -9.79325 | -47.74531 | 2025-07-11 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8a9fdd8-88f5-33c2-85e1-6a5318e555d5 | -10.90108 | -49.20821 | 2025-07-11 04:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ea6c73eb-b272-3cc5-a253-7cbc389c83f1 | -10.67475 | -49.49248 | 2025-07-11 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 09e4b0da-d7b9-3182-a7aa-d704e60ee61e | -10.56954 | -49.13901 | 2025-07-11 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a5c9cf0d-9866-33da-8cdc-cf0ca74aac8b | -13.00315 | -44.8688 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49240bd7-07d1-3978-a0b9-e463f08c6be2 | -12.02567 | -49.52281 | 2025-07-11 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ff3cc312-6676-3879-80c1-c57d551067ac | -12.9856 | -44.86956 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 888e59c2-332d-3885-9c39-9400c92a2163 | -12.19443 | -43.53746 | 2025-07-11 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b821c4b-4b39-3768-93c9-af74b2b50ed0 | -12.66506 | -47.09217 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7c40fb0f-b26b-3ac0-8f2a-068eb9234c4e | -11.44674 | -45.1176 | 2025-07-11 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a1858fa9-0c5d-3a57-84f0-9771b2305c02 | -8.22237 | -41.0809 | 2025-07-11 04:08:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4f9b5c31-21bd-3cc8-a085-b6796b17e2b9 | -8.22142 | -44.91455 | 2025-07-11 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 61212deb-ba6d-3087-9e54-1f418c9a5e68 | -13.17167 | -47.28602 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| abb83a1a-f1d7-3b89-a455-9576b6e231bf | -13.16598 | -47.27421 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd58de49-539e-33f6-bc20-a29c4245cee6 | -13.15266 | -47.28362 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| af3276b1-3bd3-3842-a423-46ba4c649535 | -7.48791 | -43.9375 | 2025-07-11 04:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6ad97eaa-196f-3113-9880-aabf8758b5d5 | -10.51004 | -44.89375 | 2025-07-11 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c48c63d5-f441-3488-b62d-af001cdc12ae | -11.95546 | -51.69469 | 2025-07-11 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1e7e0c3-6adb-3827-9df3-ee3d956a978a | -11.32964 | -45.2216 | 2025-07-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 774438e1-b88b-3f5b-bd93-209756eefe87 | -7.65311 | -45.34639 | 2025-07-11 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc62e644-a783-3ccf-b34c-2ea4c47d37e9 | -7.94468 | -44.85384 | 2025-07-11 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8eef680-f25f-3151-8ea5-e4678dc614b4 | -9.06489 | -47.89474 | 2025-07-11 04:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc8bc51b-26e0-3a19-8f83-cd0351a1345a | -12.06906 | -47.9808 | 2025-07-11 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4973dc2e-a388-362f-9f24-1f280af765ee | -11.33378 | -45.21829 | 2025-07-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aac1d2a4-d023-300b-95ad-a0c476b44ace | -8.37974 | -51.07521 | 2025-07-11 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cda15a48-bcf1-3d53-99f3-35cd87ed1f17 | -11.94968 | -46.36573 | 2025-07-11 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 028ca9fc-47ac-3409-b996-ed06898c173b | -10.67106 | -49.487 | 2025-07-11 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| b3b01c4a-00be-3099-b8e5-64bd6a521512 | -12.41993 | -43.48726 | 2025-07-11 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a31ff84-7131-38f0-9ffb-09838cd9bffb | -8.22077 | -44.91857 | 2025-07-11 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41094230-9c53-39af-945e-6cd4abc74d1f | -12.98343 | -44.86156 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3c18de6-16df-311b-8f7c-b21e65b82210 | -11.33214 | -51.44132 | 2025-07-11 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e446408a-6ec9-377d-9533-1e4361294659 | -11.84102 | -43.79169 | 2025-07-11 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c015d54f-822e-3420-826c-2f555f8ace15 | -9.53759 | -46.29436 | 2025-07-11 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 427a20bb-ef3a-39ec-8d0f-16f67a217f4d | -10.74263 | -49.8478 | 2025-07-11 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83ffd5fd-5464-31a8-bed0-4aedbbeeac40 | -12.99081 | -44.85902 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dcee50cc-11da-3a7e-847b-7c2bf0839cc2 | -9.91502 | -47.83476 | 2025-07-11 04:08:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 12571740-9e8b-3d3a-acaa-ab6d9dd50c82 | -8.21722 | -44.91801 | 2025-07-11 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95c724ee-ce7f-3305-97cc-9daebc4a2277 | -13.16712 | -47.28979 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0984f78e-b506-30c9-9fad-e0fde0f16c6a | -12.99238 | -44.8707 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abca91f9-ff15-3ad0-89a5-3ec3b1c25ee6 | -7.6414 | -44.62666 | 2025-07-11 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a46c44ef-c4d7-31f0-97e9-5632edc5d530 | -8.36546 | -43.95521 | 2025-07-11 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 264acc30-10fc-36b0-a6c5-4286845c7227 | -8.58373 | -47.19274 | 2025-07-11 04:08:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08c20951-b8ad-3c3d-9a27-c4079f9fc04e | -13.1708 | -47.29093 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5af95a5-e38b-3c2b-8dc3-5945cce65857 | -12.40668 | -45.35463 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20921c16-5c34-3d99-9e38-17a00563106f | -12.40045 | -46.36259 | 2025-07-11 04:08:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bb777fa-966f-3da5-871a-ec9cfe021609 | -13.15186 | -47.28832 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 46d48bbd-f383-3542-ab9c-f6731edac073 | -13.00086 | -46.28058 | 2025-07-11 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 558ab1e3-19ca-35a1-baae-0ce03d46be70 | -10.62333 | -45.23362 | 2025-07-11 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5f2543b8-6fbe-3fca-bc3f-7218d8324d1a | -13.00765 | -47.82644 | 2025-07-11 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ef2b45b-c0a1-3e6c-8038-473c912530e7 | -7.55491 | -45.62801 | 2025-07-11 04:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d11268d6-29e6-3d4f-a7c1-4824adfa333c | -11.84884 | -46.75489 | 2025-07-11 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e7edd29-1717-397a-aa21-7e15308c0507 | -13.13822 | -47.29991 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fc380e03-2429-30e7-803a-a9576b836c87 | -13.18257 | -45.23039 | 2025-07-11 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3b05d98d-a610-3ff5-9845-e607abdc90d4 | -13.14602 | -47.29925 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e40f0ce-82a4-311f-8903-be7b6d84c562 | -11.3303 | -45.2177 | 2025-07-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1da5e68e-2693-3426-9318-1c9577329bc4 | -8.3892 | -46.93604 | 2025-07-11 04:08:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22efde71-4282-311f-a373-380acd64cd35 | -11.57004 | -47.42749 | 2025-07-11 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46cc9b5e-0ed9-30fa-9914-c4d6c81cbe44 | -13.17915 | -45.2298 | 2025-07-11 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b8fd90e3-480e-344a-9882-197cf77a92c6 | -8.767 | -48.69629 | 2025-07-11 04:08:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c61983f-2a79-3992-87e4-94f1373e172a | -13.15549 | -47.26759 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 072a298c-1dfe-316c-a503-c705dd06c3fc | -7.5512 | -45.62741 | 2025-07-11 04:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f58efa7-afd9-3055-80a2-109670a7ae11 | -8.59401 | -47.20541 | 2025-07-11 04:08:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eee02846-8b77-37a6-aa6a-d3fda0eaa57d | -13.00676 | -47.83154 | 2025-07-11 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe4d65bb-1e35-3440-bd16-06ac0aa7ee51 | -10.68457 | -49.48968 | 2025-07-11 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a4a740a1-daab-3419-aba4-009e06724571 | -13.14279 | -47.29593 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 980f3512-6fa5-3a24-a870-57dc59726447 | -11.95041 | -46.3614 | 2025-07-11 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abb4d543-c7db-35aa-92f7-e5ae2db4030f | -7.48448 | -43.93692 | 2025-07-11 04:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| eeb3c71c-fb67-3dfa-8eb9-794d944e3b80 | -12.41014 | -45.35523 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d7502f0-bc41-3998-8439-9ee908e26e15 | -13.36408 | -47.88705 | 2025-07-11 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9aa16b01-995c-355c-bfe4-4c125b4d5a8f | -11.33443 | -45.21439 | 2025-07-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d893ad3-307d-3536-aaa6-374f7b7f05c9 | -9.8637 | -47.86907 | 2025-07-11 04:08:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f80445e-adb7-3f69-9ca8-88efd6fa0f0a | -13.15023 | -47.29794 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0056d0f-273a-3060-bdef-714e39668a9f | -10.68565 | -49.49169 | 2025-07-11 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 30e6d352-302b-3887-ad15-bfc0d378d438 | -9.61388 | -49.01728 | 2025-07-11 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 55b8693a-d08d-313b-abb5-65f2c0878c73 | -13.00157 | -44.85707 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 009c5716-b883-3837-a480-73b8dffa6638 | -13.05795 | -47.88374 | 2025-07-11 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06d77efb-1a8b-3e7d-8dd8-6fcfb5054589 | -12.4681 | -44.49524 | 2025-07-11 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d64da437-130b-360d-a0e3-38322a0c172a | -13.16622 | -47.29493 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60acb57f-6392-3172-8313-3124ed15b749 | -12.9896 | -44.86643 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5491f481-2f05-3ed4-8873-df5a6680da45 | -7.55563 | -45.62356 | 2025-07-11 04:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d782bcb3-5770-3a4b-bf22-b912c76e797a | -9.91093 | -47.83399 | 2025-07-11 04:08:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 3b263054-afe9-3a99-b1ae-4ae3dbef8141 | -13.16305 | -47.26878 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 46be5300-6d8e-3714-a127-fe4d167df702 | -12.40602 | -45.35852 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f198245-08ed-348c-b30e-d8d3c1ddc04d | -9.91161 | -47.83018 | 2025-07-11 04:08:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 4f767d63-4c33-3e0a-b54d-a17dc8ed7f44 | -9.34356 | -50.22031 | 2025-07-11 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed97b7f2-7a24-3fe7-b1b9-759e66573ddb | -12.40948 | -45.35912 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4cedf5bd-dfbf-37e3-baf2-4d7f4b408778 | -8.39318 | -46.9366 | 2025-07-11 04:08:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 823cceeb-c452-3c9d-98bc-1002980e841f | -11.84391 | -47.49823 | 2025-07-11 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| caac7eea-8b27-311c-baa2-4869d891819e | -7.55341 | -45.62574 | 2025-07-11 04:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0fe0af6-e43f-3584-925a-ff75a7791641 | -12.66426 | -47.09681 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d47b9306-f61e-3347-b2e9-0ad1dab19911 | -9.90816 | -47.82581 | 2025-07-11 04:08:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| c30dcacb-9766-3b10-9855-e195dac9bb59 | -12.98282 | -44.86528 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 027cca0c-3e42-3285-a266-a6da6d72489b | -7.33464 | -44.32539 | 2025-07-11 04:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1ed768b-d942-3cf1-ba3a-7d9a7f9b4494 | -12.40883 | -45.36301 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README14.md)
