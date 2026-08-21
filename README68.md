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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d506575-cb9e-3c12-9c6b-f69e2d71d880 | -8.6138 | -54.72318 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bd42e34-34b2-36fb-a9a2-f6e76090153f | -9.45102 | -51.60055 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 977f986a-765c-328e-b6a5-1d31fd0a3a72 | -6.42468 | -54.92827 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea763c8f-4a96-3eb9-992a-6db43b95da8d | -7.62971 | -45.76902 | 2026-08-21 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 242bfc23-efc8-32dc-a0ae-cef6c64534a4 | -6.84554 | -59.42111 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25aea9eb-0a6d-38e1-8e2b-3b79d31b7ae5 | -13.3744 | -54.38291 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 2be87036-299f-325f-8acc-954dedeab632 | -7.37673 | -59.95253 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 274da3c9-48dd-399f-9c7b-c0eca18f5aa6 | -6.36106 | -58.3326 | 2026-08-21 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c70a230-c6f6-3e5e-8acc-abdd79b6ebb2 | -6.42881 | -54.92488 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54d36923-e7c2-3b81-9ff0-287256699129 | -9.0551 | -57.06874 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd517035-60eb-3866-b005-50fc7c61393f | -15.21926 | -52.79923 | 2026-08-21 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5c48743-48ff-3a25-acc1-15f1b2fd85b8 | -8.89616 | -60.5484 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d2faa2d7-8869-3b37-b14b-93d5f89977f5 | -3.5337 | -48.18606 | 2026-08-21 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| bdc3809b-9355-3f25-829b-f681a7f783d5 | -6.86667 | -59.42072 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1b9d28b-de22-3576-a32d-028b4b17d6df | -8.5514 | -54.79168 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97bde86f-ab81-3ab7-a636-3f28ec6f4bad | -13.10049 | -51.58435 | 2026-08-21 05:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2a0d30d0-472a-30e7-b2e3-683d6761adf9 | -6.88274 | -59.40818 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 202fc71d-6186-31ad-93f5-aa498ab5e9f1 | -6.25019 | -55.4134 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d346fbf6-cea2-3166-bccb-5bc154add133 | -9.55083 | -56.79584 | 2026-08-21 05:23:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf115e3e-adab-3954-b5dd-a226788d977c | -6.11284 | -59.9051 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 24cbad85-a7b8-38bd-b5a4-dcf16f091189 | -6.09358 | -57.69994 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42eee70b-5012-364d-bf6d-8f3172d7dadc | -6.00894 | -57.86795 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c78ef66-3df6-3e5a-836a-0f5ff8f11dc4 | -7.7306 | -46.15813 | 2026-08-21 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3d5e9d95-0e31-3de9-8600-a7141f56c7c8 | -6.21879 | -55.48594 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66cc9deb-be86-303d-88bc-48ca02be8ae1 | -6.96957 | -59.3047 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 205fac7e-c426-3afe-971f-975ee68da3ff | -6.89625 | -59.43319 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cf26dac6-f7f9-3745-9ef1-f7f687e9f0be | -8.05696 | -50.1116 | 2026-08-21 05:23:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4390f877-b0f2-3d70-aa9f-042e7794d719 | -13.39703 | -54.36541 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 67e5a99e-4332-3f98-85a9-086e92df8f39 | -6.66887 | -52.89367 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7fef35c-ecc5-36e6-bba0-0f780507aaf9 | -8.59599 | -54.74236 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4b4443e6-8174-3558-86e4-d991dc57d8f5 | -8.66676 | -54.58908 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2290d6a4-7a0f-3268-9fd5-ba1ba355f168 | -15.49267 | -53.90257 | 2026-08-21 05:23:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| adc49344-5626-3507-a72a-e79eb079a403 | -8.54343 | -55.32085 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 831655fb-f97a-3c96-93f8-3bb23341c279 | -8.58871 | -54.74128 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fdbb486-611f-3592-b3f6-c13dae2a3de0 | -9.20768 | -59.76919 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7b8c413a-4071-3e70-a2a2-0bd0c5c59a95 | -3.54501 | -48.18156 | 2026-08-21 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2e72e175-09ae-3110-a04e-5313861bdbaa | -8.16081 | -55.37536 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 141d4f65-0c91-385c-92f5-88b9028bcf28 | -6.85904 | -59.44611 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 985ade23-0b2a-32a4-ba59-32f1a61ff79f | -6.66438 | -56.34792 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 24d7879f-484b-3c42-b520-31ac5c31d090 | -6.87051 | -59.44037 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 25fa13da-5c94-361b-b7cc-ef5ad925943d | -6.11117 | -53.07315 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9134c0ab-5ccc-3929-8fb9-f85023a56e3c | -4.11534 | -48.92921 | 2026-08-21 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d7a93a3-e1a7-3b82-8c89-5176eedeef92 | -9.45835 | -51.64615 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58a23c43-0542-33a0-adb3-231e0c4753c5 | -7.60343 | -60.83294 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03aae136-ba85-3f68-88d8-7a4aff3cc904 | -6.79923 | -59.45177 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8859771-e144-3a9a-9b18-94b4488a5035 | -6.69099 | -59.10278 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d117ff9-965f-3c52-b05b-b48bf64322f4 | -6.70437 | -58.9342 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 000699ab-2df5-3073-96ca-a2a83edd25a8 | -6.65147 | -56.34224 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3400928d-2f3a-3456-ad66-12a254f33782 | -6.23162 | -55.40361 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 946216d9-fad1-3a18-9eb2-3642f6776004 | -4.94065 | -55.78214 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b3c6a31a-c889-3e24-86a0-e3601f1b8820 | -8.57651 | -54.74813 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f00f92c1-6085-396a-a52e-01c33ec89a55 | -6.88257 | -59.43094 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 39b89769-3ea3-3a42-ba5c-8f71253d2350 | -3.26388 | -49.52356 | 2026-08-21 05:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 491f3b29-7de1-315f-81d5-bd5e65093abf | -6.80937 | -58.99912 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d7e9799-ae8e-30a2-95f4-5134e91e9a3a | -6.08986 | -57.91283 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2743ad3-62ae-383d-92ef-14d09258386f | -6.09413 | -57.69646 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a02c3ce4-e966-3953-bd31-db81ecbbc2e4 | -6.42164 | -52.76266 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8050728f-fbd5-36b8-becd-a7e36f59e56c | -15.76748 | -55.55918 | 2026-08-21 05:23:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dead19ee-2483-329e-9a16-6111d310baa4 | -9.79805 | -46.64853 | 2026-08-21 05:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9f1ad30a-dcac-35a3-86f4-b59a0f44766c | -7.7768 | -61.16156 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 32a008fd-c443-34e0-9b8a-b4b2a23c4788 | -6.2228 | -55.4828 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7d58a4a-91a0-339d-a13d-11d4f0059d2f | -6.58343 | -58.97065 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b1a88c1-e25b-3ff3-8dd4-7a39255d121f | -6.92709 | -59.35057 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f53782a7-6ce0-37b5-a761-32a0b850770b | -6.86427 | -59.43554 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 42da0389-f691-3785-bbcc-1bea66b77196 | -6.86306 | -59.44297 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 18787f15-16bb-3648-8bb0-f236cdb45c49 | -6.69763 | -58.93306 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32224d98-cb85-3636-b35d-cf2889a33b11 | -13.40025 | -54.37118 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 8bd88a6e-caa0-323c-bad1-e463521113fc | -8.58297 | -54.77929 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2097655b-178d-3cd0-b48f-95ab12b6c0e8 | -7.02027 | -48.04069 | 2026-08-21 05:23:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2482df99-28dd-3760-a9e0-49d538902e6a | -6.00064 | -57.83457 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6bddd39-41bd-39d3-a545-40195ef85fb3 | -9.11585 | -60.33217 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bdbbcfd-0038-3b11-800f-057254d34a3a | -4.04978 | -50.30042 | 2026-08-21 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81bdf8c9-fb99-3096-908b-4fbf000ff411 | -6.90118 | -55.22457 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ce645f8-e6b9-3a2d-a4bc-6ab23d7a59d9 | -6.42837 | -52.76115 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7284a163-f200-345a-926d-a064dc61ed57 | -6.76719 | -59.45419 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67c93257-07af-3fce-9659-fdf6030f6bfa | -6.58271 | -58.99653 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e773dae1-8d80-31db-8f7d-55357c660c4b | -9.21269 | -59.78135 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3d7ddba-c7fc-31bd-9130-1f03a67806e0 | -7.60963 | -60.97544 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33b3c89f-5f06-34df-850e-f41e45a50966 | -7.88952 | -61.66945 | 2026-08-21 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdd9fc47-1c36-3850-8c63-7417936c9c87 | -6.86246 | -59.44668 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 788db340-44c1-3ad2-9dc6-7e2eaadd0f72 | -9.44861 | -51.61784 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| edf7472c-a98c-3e83-b793-7f3f68f82a1d | -8.54462 | -55.31286 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ad9fac4-5dc7-3deb-a54c-44d4c72113e7 | -6.43029 | -52.73243 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56a3eb68-f69f-385b-b06c-fdce9af71148 | -7.77457 | -61.1524 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| bac5c9e2-dcec-375d-9a1c-af900ff6f6ef | -15.16281 | -48.77922 | 2026-08-21 05:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8973c825-0b98-3fa7-a1e2-14455945fbff | -6.93561 | -60.08538 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b3f352a-797b-33cf-9207-6f5bdd989b23 | -6.24718 | -55.39445 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b9da405-1310-3a06-8d4e-4d2c550e39b0 | -7.07012 | -59.97142 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 083844e1-728f-3695-aeef-15718fc4969e | -8.49306 | -54.87792 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb25cd30-67d6-3745-9a62-2d6b4913b774 | -5.60367 | -44.0046 | 2026-08-21 05:23:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| af50d761-d53d-320a-a6f7-6fbbf9287388 | -7.37326 | -59.95198 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eaf83720-eecc-372c-95fb-52604a613d4d | -8.18279 | -54.99046 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f22b6c0-69b1-38ee-9e71-e597887cdd56 | -6.1122 | -59.909 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6d7c652e-9327-3c0c-b97a-595e0ec4e173 | -6.4295 | -52.73758 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3db9aa1-5737-31f8-968d-9d27eacfe406 | -6.87795 | -59.4378 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 406fd794-2578-34d0-9252-b1d32dfd1d6d | -12.51578 | -54.76676 | 2026-08-21 05:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 395bb00d-53a7-3a3d-9e57-90104fe541e4 | -8.50272 | -54.87009 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a1134fb-3d05-3b21-a74a-f790d5a975bc | -6.86581 | -43.74398 | 2026-08-21 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca60be94-7c23-356a-a979-2771eecc16a3 | -6.79819 | -59.43634 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f966e8f8-46f1-3123-800e-edda88cd5569 | -5.66808 | -51.64821 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README69.md)
