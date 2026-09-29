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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9671d3da-178c-3aba-a4d6-a644c66164c9 | -7.52114 | -46.61407 | 2026-09-29 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c7d08a0b-2b3d-3831-9189-099e1e8c5adc | -9.76229 | -36.98156 | 2026-09-29 04:14:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 7c4515dc-263b-31d3-bffc-a648475dad92 | -8.64373 | -45.34159 | 2026-09-29 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce54ea63-3946-301d-bd3f-3313e0adc590 | -8.72828 | -44.91338 | 2026-09-29 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a2baf69-9c06-357d-95b4-388d72824601 | -6.14478 | -51.73788 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23a185da-86d0-3a3b-97a6-e45243536f33 | -8.65441 | -45.33962 | 2026-09-29 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 391d8eea-a7c2-3f79-b5f5-ae2aa554bbc9 | -7.49529 | -44.55597 | 2026-09-29 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b21539e5-5dd7-3ffd-a829-88de66a49fdb | -5.73303 | -43.27911 | 2026-09-29 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3bc77591-91e1-3ae0-8b6c-8f6abde34b54 | -5.09138 | -44.84268 | 2026-09-29 04:14:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1862c08-7260-388d-a247-c8928834f86e | -3.96591 | -48.89714 | 2026-09-29 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2e7cf3f-cf38-37e8-a450-8b63ac736eba | -6.15387 | -52.90327 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b00432f-9ccc-3001-a7ec-5f948aa8b5cc | -6.17403 | -46.74786 | 2026-09-29 04:14:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52e7866e-028a-3274-b8f8-304afd4d4118 | -7.92886 | -45.48665 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4f90bd2-804d-3d70-addf-8af1133578d6 | -7.24978 | -43.37017 | 2026-09-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d7a7aafb-3c9c-3933-9ed8-98f6a4853eb7 | -8.63546 | -45.30666 | 2026-09-29 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c47a0c60-a4d7-38e5-b544-ab6937baa05e | -9.02167 | -45.01895 | 2026-09-29 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bbeaa37d-ed45-3f26-a107-272aae8446bc | -6.90858 | -47.00816 | 2026-09-29 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abe548fb-193d-3a1d-b7bd-fb72279ed492 | -4.81923 | -45.63926 | 2026-09-29 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ca8cf142-8bc0-3af1-a4c7-f0668f7d7227 | -1.33039 | -47.78698 | 2026-09-29 04:14:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a32a0402-709c-394e-bdae-141ef637d3fb | -5.73249 | -43.28255 | 2026-09-29 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b6ba286-1126-39c3-a7fc-00bc4b677000 | -6.99294 | -45.34175 | 2026-09-29 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdd03ebc-612e-35a5-8465-a9305b9ee2a6 | -5.85662 | -47.42412 | 2026-09-29 04:14:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c69b9f24-864e-3490-a6ad-85efc0cbcf45 | -5.73682 | -45.1791 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fb757c06-313a-3850-a406-1ba261666de2 | -7.38358 | -42.1288 | 2026-09-29 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2328277d-30bd-3242-b8e4-f137eb83218b | -8.97699 | -44.16002 | 2026-09-29 04:14:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b36df244-9e96-3f55-8724-c392be6358a5 | -3.59406 | -50.68248 | 2026-09-29 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 021e3e8f-559e-310e-95d7-98b15718579b | -3.9583 | -49.051 | 2026-09-29 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d3f01da-2b50-3636-bf22-a583997b80bc | -5.73234 | -45.05241 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2ca7935-b872-35f4-a82e-b2fdc78570a5 | -7.99538 | -43.25396 | 2026-09-29 04:14:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aa14e396-9426-30fb-a2cc-2bc90bc628c2 | -7.92545 | -45.48612 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bdcb8e20-c55c-3cad-b79b-acdeebf240f5 | -5.73798 | -45.06095 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 842a822d-15e9-3e67-9917-fdb57a28f490 | -8.23444 | -45.40278 | 2026-09-29 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47bb2326-1f4f-3439-aaac-257a8eac980b | -7.43287 | -46.87585 | 2026-09-29 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 62491aa3-b7bb-3f33-9e30-8cc5b897f4bc | -7.56758 | -47.36669 | 2026-09-29 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7ce99f7e-a3f9-3463-8b7e-15ec01e3a9ed | -7.46471 | -45.81814 | 2026-09-29 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dfe2b091-c97c-3bae-9efa-1c2c634f0bba | -7.47003 | -45.80708 | 2026-09-29 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2639ed08-3c0f-3010-808b-da50ca3d0575 | -2.57846 | -50.78867 | 2026-09-29 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c0b2d44f-fcf0-3820-87bb-5f74becce804 | -7.38871 | -46.42683 | 2026-09-29 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a10805ee-85b7-348f-a26a-129d2e4c7559 | -3.99107 | -49.04309 | 2026-09-29 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e57fea15-97eb-37c9-8ae5-f94c3f45ae94 | -4.67676 | -44.57976 | 2026-09-29 04:14:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a20d4204-f173-3075-a203-500ffbddc4f3 | -7.06381 | -41.74675 | 2026-09-29 04:14:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 943761f2-7147-3090-997b-b401c1dcc922 | -7.19008 | -44.96065 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c2042a1-c080-3134-8421-f9ca3dd95899 | -7.07619 | -41.73366 | 2026-09-29 04:14:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e04258aa-42a6-350c-99a8-cd06d1fbe7e3 | -5.73569 | -46.39508 | 2026-09-29 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 72b6405b-5458-331f-9f46-c2473921439d | -5.03379 | -43.57144 | 2026-09-29 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 309c27f7-a68b-3021-8997-3a48f222ff20 | -6.15258 | -52.91065 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 159dd279-5cb2-3bd2-9a32-306a1c0b1cfe | -6.39707 | -44.84956 | 2026-09-29 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0219f987-7128-3c6d-895a-7995cf14c10b | -3.96267 | -49.05178 | 2026-09-29 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29167be7-7ca7-30d5-a512-6589936a9d25 | -8.24823 | -45.44657 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 995213c7-b1eb-3dc8-98b0-b05daafdfa71 | -2.94839 | -48.98602 | 2026-09-29 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46022fa9-fd3c-3b77-ad75-2ae43538eea6 | -2.39024 | -45.17252 | 2026-09-29 04:14:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ba46bd5-e267-302d-98ef-b814f09473fa | -4.13318 | -51.06196 | 2026-09-29 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd702a8e-d932-32ea-8a88-a069998228b7 | -6.32208 | -52.62014 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc9a4991-d7fe-3cfb-9dca-786304385ece | -7.4135 | -42.61982 | 2026-09-29 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e7a2e92c-32cb-36f4-9242-bf4d8dfaaf39 | -7.39362 | -42.63831 | 2026-09-29 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a289562c-4bdc-3961-972c-94821ebb4398 | -5.72686 | -53.46345 | 2026-09-29 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dacfbc75-e828-3c71-90a6-bc26223a29f6 | -2.57894 | -50.78572 | 2026-09-29 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3854c40d-058f-3410-a348-161291c2ae32 | -7.68016 | -44.89138 | 2026-09-29 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70b7b4a4-fe37-3d86-b676-5bc08b1a4b51 | -3.6922 | -39.57969 | 2026-09-29 04:14:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 10.4 |
| e3788548-f6f8-3d9d-a0eb-463c9fbd7137 | -8.96984 | -44.16245 | 2026-09-29 04:14:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f3646c6-7e36-3c19-96ec-4f9575d0a5ec | -3.95642 | -47.63981 | 2026-09-29 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20f00c6b-7345-3d18-9f62-77b9536e6783 | -5.72181 | -53.45856 | 2026-09-29 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f95483b-37e7-3c27-8caf-7b48787ddecd | -4.12785 | -51.06115 | 2026-09-29 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25b95d51-b296-3c63-b121-c53d3ada1f4a | -8.22368 | -45.46926 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e0fc749-1813-3183-ab5c-bab26079bc0b | -8.96872 | -44.14803 | 2026-09-29 04:14:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18260b37-2181-34db-87e8-1cf5b5282b1d | -5.19207 | -42.97141 | 2026-09-29 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f1570a88-be40-34f2-a6d6-2e08da2ed880 | -5.08797 | -44.84216 | 2026-09-29 04:14:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26d93488-6812-3156-afdc-f82178e7788a | -7.24797 | -45.26139 | 2026-09-29 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fb0bac6c-bf6d-3227-b612-2124013963e2 | -4.81636 | -45.63467 | 2026-09-29 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 254c3c66-4ac7-3e1b-9236-375e70830629 | -7.53469 | -45.88359 | 2026-09-29 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14510620-0da1-3fd0-8cef-98e5f5625fbd | -3.70618 | -54.21834 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 510b2bde-61d1-3b87-acb6-fe7af682b92d | -6.1453 | -51.73487 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14d45c04-7094-3333-b43e-385df6d45f12 | -8.36191 | -45.4383 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f20a979e-f1f3-3892-8596-2eb0ee533800 | -5.7386 | -45.16782 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d97384b8-439e-3ec9-b815-20dd3c7910e5 | -5.61076 | -44.99974 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a2ab0ecf-ead2-35ac-8ef5-6f0ab7718851 | -4.07773 | -40.51446 | 2026-09-29 04:14:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c81b5592-f390-305a-a760-dde59033835c | -8.24584 | -45.46137 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab1d3620-49ed-3b48-9a30-f89a78d108fb | -7.33247 | -42.08044 | 2026-09-29 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0eef7dc4-35f9-3bcd-b57b-25e18af2dda1 | -8.7674 | -44.15113 | 2026-09-29 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99641921-789d-37c1-82e8-6d8484ca46c1 | -5.8522 | -35.30444 | 2026-09-29 04:14:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5e6d9785-5241-3dcf-91f3-eb62842cf738 | -3.71325 | -54.21444 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f5027e7f-de91-31f2-aa2d-a65fd82b8588 | -5.43465 | -43.44359 | 2026-09-29 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a902692b-cfa0-3e32-bf9d-ad31f9dcd561 | -5.43081 | -43.44652 | 2026-09-29 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 33226512-9ce7-3480-9e9e-a62561dd940b | -2.98646 | -54.53716 | 2026-09-29 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dc5b0590-62b5-352a-a5f8-26a4be44d6af | -7.41029 | -40.22263 | 2026-09-29 04:14:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| abd70bdc-99f2-3605-b697-0cf3257e993c | -4.42208 | -46.28212 | 2026-09-29 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e946e736-d18d-3fe1-aead-92c3225e6310 | -3.26659 | -50.1352 | 2026-09-29 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3c1440e4-c565-3f75-8704-2ce812e23057 | -4.08028 | -40.51416 | 2026-09-29 04:14:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 02899fe8-cd8e-3cf1-a3d6-558262f143f9 | -6.74619 | -44.83846 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3471501a-4f88-3dc8-b334-7d520572938a | -7.40304 | -40.22153 | 2026-09-29 04:14:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 49d80f00-038c-36ce-aa5f-90dd5e25a450 | -6.13104 | -43.73426 | 2026-09-29 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d7e1e5df-977e-32cb-a380-4ace79fc1282 | -7.99814 | -43.25795 | 2026-09-29 04:14:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d1203ee1-9e10-325c-a89a-61dc0c40a962 | -8.66176 | -45.34801 | 2026-09-29 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f01d68fc-0267-3c9e-9bf2-54e173f49530 | -3.15633 | -54.08567 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c213527b-ed96-343f-873b-cb1b35edb4c3 | -6.17036 | -46.74731 | 2026-09-29 04:14:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 392a32c4-4ad0-36b0-9b9d-827d81037ea8 | -6.31552 | -52.62606 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1d729a81-79b1-316a-858f-59529531be36 | -5.73116 | -45.05985 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 10b02d52-01c5-3251-88e2-612008374bbc | -6.14772 | -52.90609 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6db3163-ad66-3fdf-a20b-639d7bd3c111 | -2.29104 | -48.58162 | 2026-09-29 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ac57dfd-dc6d-38fb-a73a-41b4b9ffa9ff | -6.99635 | -45.3423 | 2026-09-29 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README16.md)
