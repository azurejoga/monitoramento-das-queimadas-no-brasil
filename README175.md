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

## Dados Diários - Página 175

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68883b83-9f6b-3860-81f3-06d84750dedb | -12.21651 | -57.10373 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2ea93508-927a-3740-86ee-11c4d9523887 | -12.19326 | -57.13037 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bf114b1-9010-3d6d-9f98-42c3f58c4ccf | -15.51785 | -50.39618 | 2026-10-09 05:06:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2095aa7d-243c-36a2-9d82-be53bdbfa0e0 | -12.20781 | -57.13296 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8e51af2-042b-361f-b3ab-337890eff7a8 | -13.05822 | -55.62109 | 2026-10-09 05:06:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 639431f9-e110-3194-975e-3d59fbfeb006 | -14.96731 | -47.54187 | 2026-10-09 05:06:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c6c2055d-df27-3ac2-948c-84e619cdddbc | -12.21288 | -57.12511 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ee4bf890-fd83-300a-82be-b03519e79510 | -12.21943 | -57.13067 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f180fbd5-79dc-3065-8119-9104db314676 | -13.20678 | -47.87312 | 2026-10-09 05:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fac4e41a-5a22-390b-b85f-63213d42c05a | -11.7929 | -46.79968 | 2026-10-09 05:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 746c83a5-11e6-317a-acb3-7775cc707b09 | -12.23683 | -57.09414 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b87867ad-8ff8-30b0-9296-ebb0f1e61f4b | -12.22235 | -57.13557 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f2d0937-83f7-3850-a161-29e510e28d4e | -14.93032 | -48.08879 | 2026-10-09 05:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ee2bf94-5bf4-3383-a44d-b2c1d099b889 | -12.20053 | -57.13166 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14b985ff-407d-3da2-a244-74e7171bbf06 | -12.2216 | -57.09581 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 6044338a-2b9b-3b9a-9263-d600e7ecf444 | -12.21941 | -57.08667 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| bf9a4787-ddc1-3c20-93b2-56ce13a219e0 | -13.19969 | -54.36044 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16d5d5f4-e5e1-330a-b60a-dbec16469793 | -11.97511 | -57.61156 | 2026-10-09 05:06:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59e9672d-ae22-3c8e-8d45-1c802dff7bb8 | -13.16363 | -54.3508 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c36fb9d2-e629-30c6-bf25-6dc128e10e54 | -12.2107 | -57.09393 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 08c538e8-1e13-36aa-bef4-e898e67d6ba8 | -13.16654 | -54.31119 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4afedda-3e03-3037-9e96-e4b44784e461 | -12.24265 | -57.104 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 47601584-bd12-334a-be6d-416fc08c3ce0 | -12.19399 | -57.1261 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16b2a163-d6d5-3d5c-b995-7b1f69d8ea9d | -13.90569 | -48.90954 | 2026-10-09 05:06:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 61f0a8f9-51f0-3e91-9bfd-5145cbb9ce92 | -13.19913 | -54.364 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5dd6ea95-0586-34e8-81cd-7cda26650033 | -13.16396 | -43.2826 | 2026-10-09 05:06:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| eba2aea8-48bb-33aa-a885-fab1e7efd45d | -14.87891 | -50.2961 | 2026-10-09 05:06:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2f4bd3e-0c9b-3231-a5c9-867933703730 | -10.85458 | -59.1215 | 2026-10-09 05:06:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e1956d1-d9b4-33a5-892b-c2fe28628111 | -13.15753 | -54.34614 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7601962-5bae-3de7-9220-377cba293c42 | -12.81504 | -44.65176 | 2026-10-09 05:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9a41146-cf10-3d10-b78f-b5c2143e4332 | -13.11269 | -46.34794 | 2026-10-09 05:06:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98c2e49a-737a-38bd-9c61-874a0fead24a | -12.19355 | -48.41496 | 2026-10-09 05:06:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc4e009c-ee78-32dd-9891-1db3e6be7f88 | -12.21215 | -57.1074 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 991c1c1c-8aef-343e-aa50-bbaec418a38b | -16.57235 | -51.62672 | 2026-10-09 05:06:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9e5a770-cd14-3389-ac87-f23ba4e164b1 | -12.23611 | -57.09839 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b92a8bd6-c695-36c4-bd21-f37643906ebc | -15.10029 | -43.63828 | 2026-10-09 05:06:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 53fded81-798a-3f09-b9a8-bd83d45abd0d | -13.80754 | -52.79413 | 2026-10-09 05:06:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12840b27-7e9a-3c70-ba68-4c495a440616 | -13.16972 | -54.35546 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61c84e38-8be6-3022-beab-4c1fb4d25fdb | -16.79502 | -52.06535 | 2026-10-09 05:06:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eecf640e-b584-325b-b6e0-9e905f7b214d | -13.15364 | -54.34913 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| e4684aca-be88-3282-a34f-ee60ab5af5bc | -12.17582 | -57.10098 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d832536-c91c-3d81-a0d1-1368aaae902b | -14.7399 | -48.217 | 2026-10-09 05:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d8d0496-8d71-31c1-b2d4-bfb8daee1758 | -12.22231 | -57.09156 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 52c536fb-8f17-3b7c-902d-c3b2ebea14d4 | -10.85526 | -59.11767 | 2026-10-09 05:06:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67163d14-eabd-3ffb-ab4e-a337ae2e6a50 | -18.32828 | -42.37309 | 2026-10-09 05:06:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 3201e98d-d17c-3318-b540-c83e0e32ab9e | -15.44344 | -45.43931 | 2026-10-09 05:06:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01f8ff57-0ca7-38e2-bd5b-a7793eb7f219 | -18.08247 | -42.2639 | 2026-10-09 05:06:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| dbdedfcc-395a-3c35-a85a-eeb2b3bae7a4 | -12.22667 | -57.08794 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| bb4c9b42-2dc8-36bb-b5fc-116e97299b6f | -12.20344 | -57.13657 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 087ebb98-b9a2-37dd-acec-0242ccc3465c | -16.57597 | -51.6273 | 2026-10-09 05:06:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11652753-c43a-306e-b06b-79d4805c8f46 | -11.75355 | -61.06575 | 2026-10-09 05:06:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 67f631cc-8d42-3609-a04c-12dc125a9bbb | -13.20132 | -54.37166 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 81f6dbbd-18c0-302e-b7d2-cecffbb027df | -13.17191 | -54.36312 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5b21aab3-7d93-3f69-9dbd-2b85465a61cc | -14.43953 | -43.93098 | 2026-10-09 05:06:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e68e2ff0-b9ad-3965-b9fc-b1d307cf5910 | -13.6392 | -47.67513 | 2026-10-09 05:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 211817c5-a643-325d-99ef-c4913794e56c | -16.28967 | -48.01933 | 2026-10-09 05:06:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ec447638-5956-30fd-b91b-fa81b6e80825 | -12.42753 | -57.22572 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| feffabc7-cd8b-399d-b438-825d44ba423b | -13.02782 | -46.81459 | 2026-10-09 05:06:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 122df1d8-eaca-33d1-a692-362388bc7378 | -15.78224 | -44.68039 | 2026-10-09 05:06:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a151e3cf-1111-315c-b654-3e244124a6f4 | -11.99458 | -57.61045 | 2026-10-09 05:06:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d471749-ee51-3901-97e1-3300d0598d5b | -15.10623 | -43.63894 | 2026-10-09 05:06:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e3ca5417-748a-3cd4-9cab-8ae44b6ea1f7 | -12.21508 | -57.13426 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 05314abb-026d-3f2f-8e89-df7ccbcf5bf8 | -13.80698 | -52.79782 | 2026-10-09 05:06:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fb7e22a1-fa4b-38a6-a8b4-6c70c247ba9e | -12.24337 | -57.09973 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 36a38b70-166a-3b16-a361-4b56ef1cb317 | -13.63527 | -44.42181 | 2026-10-09 05:06:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 777adf31-bf98-3736-997a-c11114222194 | -13.50126 | -44.37107 | 2026-10-09 05:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a74a8be4-51ca-368b-9ac1-76fba74a4f1b | -12.30272 | -47.05608 | 2026-10-09 05:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d336f4a5-4ebc-353f-8cab-b618426fc767 | -12.81545 | -44.64834 | 2026-10-09 05:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db78341d-6bd2-3efc-a2de-5d3ada6c3ae8 | -10.6813 | -58.73551 | 2026-10-09 05:06:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6dcade4c-2778-34bd-8a77-d6916eff2cd2 | -12.23105 | -57.10625 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 01dcea87-c22c-3e63-8fdf-cc97a559ad62 | -13.79906 | -52.78147 | 2026-10-09 05:06:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf8cfdb3-3ba5-37a3-a66d-7baddc064514 | -13.1698 | -54.3336 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78e50d08-393d-3dcd-a9cf-c0ff8a8b6329 | -13.63484 | -44.4254 | 2026-10-09 05:06:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc29738a-c213-3bd9-9716-bb61ad4477b0 | -13.17256 | -54.3377 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c9c4957-ab0c-3125-9e9c-7a2d447f3d0d | -15.25404 | -42.36158 | 2026-10-09 05:06:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 02bf172c-36fb-3444-9d18-dd6f03bf6143 | -11.74978 | -61.05992 | 2026-10-09 05:06:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a86f991f-c2c1-3d8e-8f5e-959163fa7571 | -13.19246 | -54.36289 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 661833f8-7292-3562-be3d-8f524dbd5042 | -15.56615 | -44.51603 | 2026-10-09 05:06:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3290957c-2599-3fda-9bdf-88e73e1c0e59 | -13.16445 | -43.27827 | 2026-10-09 05:06:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9f9af76a-5bab-3d8d-b915-7418c24acf82 | -12.24046 | -57.0948 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf40315f-cd4f-3e6d-a423-00fa6caaa176 | -11.14794 | -54.80372 | 2026-10-09 05:06:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0817b21-637a-3a94-a305-339bfaa4b078 | -11.48323 | -54.61515 | 2026-10-09 05:06:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29115eb1-89be-36d0-8319-f09a60670285 | -11.99536 | -57.60593 | 2026-10-09 05:06:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dfbb5609-2649-31bf-9cdc-09d1d75a3a1b | -13.17653 | -54.31285 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18251487-f37f-34c6-9a3d-cb174dfb6fa9 | -14.01062 | -48.76917 | 2026-10-09 05:06:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ebd515cb-6c1a-3156-88f2-55e4fc64077e | -11.75265 | -61.07071 | 2026-10-09 05:06:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 7ddba3a7-17a5-3957-af1d-ce7961a12e93 | -13.1156 | -46.33495 | 2026-10-09 05:06:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2c43a596-87eb-3afe-a49e-930ae86f5476 | -12.22087 | -57.10008 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 12474ced-8354-3c6e-9843-848e51f485b3 | -13.188 | -54.36945 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 487287a0-c56f-3a6a-9cfd-a129b48b33d7 | -12.23468 | -57.10692 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e70e34f6-0c6c-3f6c-8b25-0c9b63d926a4 | -12.22375 | -57.08307 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a689b576-cb4a-36a7-a5c7-b4380a188719 | -11.76528 | -58.28305 | 2026-10-09 05:06:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83e83a4c-8280-3c49-8e41-01d932cab70a | -13.5104 | -48.60064 | 2026-10-09 05:06:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 178bc237-c9c1-340f-a54f-f55ca7ae947f | -14.97583 | -47.54784 | 2026-10-09 05:06:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| af5cb5a0-0045-3995-99de-3357eeb81e38 | -12.22378 | -57.10498 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7404fc56-e665-3933-879a-13e76d42eae0 | -12.5226 | -54.90493 | 2026-10-09 05:06:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9bb3ca3d-206c-399e-955b-8f02a419c3bf | -18.32512 | -42.37177 | 2026-10-09 05:06:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 321711d0-4890-338d-be36-fe4cc412054b | -13.17377 | -54.30875 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f47fca4-e191-331b-b48b-a41b6c4a6be9 | -11.9633 | -57.59086 | 2026-10-09 05:06:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 711cf531-de4f-3997-ae3d-deb89fc15b6c | -12.24117 | -57.09056 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README176.md)
