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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 813e9bb2-687c-324e-817e-aed36ffde811 | -9.2759 | -46.1852 | 2026-09-21 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 08bb413e-f1aa-3b1d-a6e4-a99c59f8e39e | -6.0196 | -51.7893 | 2026-09-21 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| cd76033a-b60c-32c9-830f-6e03b1d15fc8 | -6.7369 | -55.0874 | 2026-09-21 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 6de7b363-6606-3a03-a874-71d3adf6c7ab | -6.5444 | -44.9327 | 2026-09-21 15:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| d8f9a1c2-ef6c-3e7d-9e6a-37ce97f7dfed | -11.0223 | -54.1379 | 2026-09-21 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.7 |
| e4339b0a-1d72-3003-a100-798445c22165 | -12.2914 | -50.1633 | 2026-09-21 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 2c34068d-cc9f-3c3d-8d10-8f10e608d926 | -2.8974 | -57.7987 | 2026-09-21 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| a4ceed2c-414e-39b0-af6b-6ff29e4cf6af | -12.8918 | -52.0742 | 2026-09-21 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 630203d3-1c98-35fc-ac5f-a05d95e40fab | -5.6781 | -43.4125 | 2026-09-21 15:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| d454b032-7f9e-3016-a069-d3bc43887aae | -6.8466 | -55.2817 | 2026-09-21 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 26146d01-f17c-3440-b35a-d916c3745474 | -2.9997 | -60.8047 | 2026-09-21 15:20:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| b7007ea1-f32d-31a2-9333-000f142c683b | -10.4536 | -51.325 | 2026-09-21 15:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 4f8b85ff-0156-3a41-9a30-f17ef231a504 | -9.5595 | -66.0172 | 2026-09-21 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 96130ce1-07d8-3278-9488-291c8d4eecce | -1.0243 | -48.83 | 2026-09-21 15:20:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 3694aca6-c1fa-3e8b-b9a5-06e149a6da8d | -10.2152 | -53.9216 | 2026-09-21 15:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 7fa71f10-1337-381a-b99a-58fafd2d8226 | -11.8559 | -49.979 | 2026-09-21 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.0 |
| d8ff4ae9-114f-32d8-9400-faed7cddff0d | -6.9225 | -42.9088 | 2026-09-21 15:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.7 |
| 0377611c-8f6d-30fa-ba7d-ecaa3b352cad | -10.8096 | -50.1407 | 2026-09-21 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 190083a9-0734-3938-9316-bd79e621459b | -10.8282 | -50.1601 | 2026-09-21 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 4749bd16-df68-3e83-86f4-b35c866c10c2 | -4.0759 | -52.1259 | 2026-09-21 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| e8570f7c-fb8b-318d-847c-5995b36313fb | -5.2546 | -55.9303 | 2026-09-21 15:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 164ffd11-f544-3180-b050-cffa590f128f | -6.7123 | -58.9412 | 2026-09-21 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 0c121aa6-8831-3ddc-8a36-160737226fdb | -8.5984 | -54.6139 | 2026-09-21 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| e2e2bfd5-6f5b-3e98-a8ef-15593b3b48aa | -10.4675 | -50.2624 | 2026-09-21 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| d2b8fa52-4861-3c0c-9807-4346ca5ea45c | -7.326 | -55.5953 | 2026-09-21 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| d411f956-cd79-33d0-b3bf-d118d9a77005 | -11.8359 | -50.046 | 2026-09-21 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 7237d0ba-3c54-3739-9821-c3643b9ff551 | -4.2964 | -56.2596 | 2026-09-21 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| d77e3561-7863-399b-875d-f52a8332f9ca | -3.3823 | -50.4486 | 2026-09-21 15:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 599e6963-e125-3291-9ac3-7fcc9fc0b15b | -3.478 | -59.5779 | 2026-09-21 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 111.5 |
| a86cca5a-6ff5-35f5-92d1-6d0b4e8d3793 | 1.058 | -51.165 | 2026-09-21 15:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 22497a00-fb72-3b25-aec9-bedf9d0e5c35 | -10.6189 | -50.2466 | 2026-09-21 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 5c621dbf-3f13-3a43-9d38-01f4f9cd19c4 | -9.5593 | -66.0545 | 2026-09-21 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.3 |
| f98a3550-e8e9-3d4a-bcc2-d2e13bd1d5dc | -10.4486 | -50.2644 | 2026-09-21 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| f85d4cc8-a21d-3fd1-bc3e-e77acc3bf347 | -11.0407 | -54.1772 | 2026-09-21 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| f682c3b5-9fd5-35bd-a2a4-9ed58f2eb24f | -9.8692 | -48.4033 | 2026-09-21 15:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 144.3 |
| b57db242-2cd0-3538-aeab-b928b7466dfc | -10.955 | -50.5738 | 2026-09-21 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 2b3a8cc4-3f84-3861-8052-01b4da847167 | -6.5571 | -45.5434 | 2026-09-21 15:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 133.4 |
| dd948ce6-6501-3405-aeed-86dd57cdcdce | -6.7691 | -58.6873 | 2026-09-21 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 153a5aaa-a2a2-3d95-8caa-1f9123645c62 | -3.1881 | -58.5855 | 2026-09-21 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 3f7facbf-a831-31b7-9da8-8f1fb56cf042 | -9.1523 | -49.9853 | 2026-09-21 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 021e0299-7274-30c6-9e5e-f03387977893 | -12.5227 | -50.0267 | 2026-09-21 15:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 0ac3e533-1fb6-3de3-b255-5c142b1d8c5e | -4.4303 | -55.0867 | 2026-09-21 15:20:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 1dd252d3-7e1f-35c3-b96f-d0f9f7221869 | -10.2982 | -50.2158 | 2026-09-21 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| a24cdb37-c0ae-3879-9fb8-29e25ea8b87c | -6.5634 | -44.9084 | 2026-09-21 15:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 250862ad-ff6d-3782-81d6-de4ae1e2b6e1 | -3.1698 | -58.5859 | 2026-09-21 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 451b46ac-722d-3737-ba74-bba15ab456fb | -6.3196 | -59.9956 | 2026-09-21 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 79ed3735-168f-3f13-819d-01ca1c06479e | -9.3986 | -48.3213 | 2026-09-21 15:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 9c174257-4382-31db-a640-385803319b25 | -8.7706 | -45.8567 | 2026-09-21 15:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.3 |
| c8a5e161-07e9-37dc-8899-20e9b07cb438 | -12.1853 | -50.8623 | 2026-09-21 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 176.4 |
| 19dd12ef-e68b-3baf-8ad1-30045ac30578 | 1.0213 | -51.1447 | 2026-09-21 15:20:00 | GOES-19 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 656b9a4d-0268-33f4-9209-7d9019795488 | -10.6755 | -50.262 | 2026-09-21 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 86de481b-0e04-351a-988e-5aa051ea39b8 | -9.831 | -48.4292 | 2026-09-21 15:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 24f04b3e-662c-37c2-91a2-12a741d94c57 | -10.9358 | -50.5972 | 2026-09-21 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 3b68db66-896d-3de8-9a32-f586507fbcd6 | -10.4672 | -50.2838 | 2026-09-21 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| ef946b6d-36f2-3c35-8322-4e9cdb0a15d9 | -3.4186 | -61.2895 | 2026-09-21 15:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 914b6af4-ba68-3346-89be-ece64d76cc86 | -6.5759 | -45.5419 | 2026-09-21 15:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 7c05877a-6e43-3711-ac36-a338a25a96ce | -7.3259 | -55.6153 | 2026-09-21 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 988ce9a0-da5c-31b3-b732-628a10929556 | -8.6169 | -54.6328 | 2026-09-21 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| cd48f534-72f1-3e97-933a-bea2011ced9a | -8.0894 | -55.331 | 2026-09-21 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| adc3ffcb-153f-3d3d-bdff-a8ae40eef09f | -1.1345 | -49.2123 | 2026-09-21 15:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| d2217ad9-8e90-3d10-9046-aee4af780904 | -10.8743 | -50.9439 | 2026-09-21 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 5933d1c3-040d-3e79-addf-d3d44046365e | -10.4728 | -51.302 | 2026-09-21 15:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 213.9 |
| c99696a1-6dd1-3e50-89e1-d3e8e869ab1e | -8.5982 | -54.6341 | 2026-09-21 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| a2216490-401f-3259-9bf7-a781cc222844 | -6.8448 | -55.5411 | 2026-09-21 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 5be4aa9f-60c1-3505-857d-de9ed94fa5e4 | -10.8197 | -50.7797 | 2026-09-21 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| cdecf542-c842-3e8d-8ac5-fb36535b973e | -10.2635 | -49.984 | 2026-09-21 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 4a5a8066-1246-34ff-bb13-78dcb04f5728 | -6.583 | -58.9658 | 2026-09-21 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 1f84d5ea-02f5-3475-8707-5605ddfad71b | -13.2407 | -51.7784 | 2026-09-21 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| bdf527ba-2015-3cf8-8606-19d9ddd052f1 | -11.8168 | -50.0482 | 2026-09-21 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 8d193bb9-f8b1-32f7-8ccd-aa93fd2cdd5c | -5.6594 | -43.4139 | 2026-09-21 15:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 171.0 |
| db15292d-8f85-3dd2-8755-5e2c4e678ac4 | -3.4599 | -59.5209 | 2026-09-21 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 19525a80-8446-34ca-90de-2b4f785e30cd | -11.801 | -49.8345 | 2026-09-21 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 9d255793-6acf-3086-b5e6-52c4571cc910 | 1.0397 | -51.1237 | 2026-09-21 15:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 83.2 |
| d358762a-75cf-3ead-96d5-21dbf154fbd2 | -10.8735 | -53.9668 | 2026-09-21 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| d9c3fb99-7f0c-3960-af96-22d995646320 | -10.2154 | -53.9011 | 2026-09-21 15:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 1cb70770-df5a-3ec4-a468-94a647b318d3 | -10.473 | -51.2808 | 2026-09-21 15:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 132.0 |
| 28d2b360-f238-36df-bcdb-7f80e3f6eaa2 | -5.804 | -53.5223 | 2026-09-21 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 357b160e-481f-367f-802b-9ae272e81a5e | -5.6221 | -43.3934 | 2026-09-21 15:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 177.3 |
| bc0371ad-a828-383f-8b01-7cee104c1213 | -10.3363 | -50.1905 | 2026-09-21 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| bfcf66f3-6999-330f-8745-8527021d3e17 | 1.2424 | -50.9346 | 2026-09-21 15:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 200c4be1-913d-3e03-8af6-600d2ed30f61 | -10.3546 | -50.2313 | 2026-09-21 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 7feaa4ef-6f51-3f9f-9834-1516dd654a42 | -9.1056 | -60.9703 | 2026-09-21 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| c59ae463-84a6-30f1-b6db-17d281978d01 | -10.8732 | -53.9874 | 2026-09-21 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 15929ae3-251d-3d32-a71c-cabfabc22679 | -10.6565 | -50.264 | 2026-09-21 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| a17b5ccd-0dbb-303b-82d5-d6813fcc35df | -7.5661 | -61.3239 | 2026-09-21 15:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 3afb1c02-7a53-3938-af25-2516505744bc | -7.3376 | -44.4744 | 2026-09-21 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 94611271-b749-3ac8-93f6-67e07625a727 | -6.5569 | -45.566 | 2026-09-21 15:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 5e2a8f99-4939-3112-9ecb-9aff2d0e0092 | -9.8307 | -48.451 | 2026-09-21 15:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 160.5 |
| 3ba3d926-4ab6-3ed1-9e2c-fa91dcb8a07c | -9.0222 | -51.5184 | 2026-09-21 15:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| f2d7d63a-d038-327c-972e-e1f743ef86b7 | -11.3419 | -51.3606 | 2026-09-21 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 139.0 |
| ca883cc5-9a52-3a42-abc5-e7835626feb7 | -11.8014 | -49.8129 | 2026-09-21 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 9a5d88fc-a0c3-34a0-b594-3e3a65eaa46a | -7.8243 | -61.409 | 2026-09-21 15:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 34899d47-4228-37a4-8d32-7b0905f31358 | -10.8093 | -50.1621 | 2026-09-21 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 0c488b02-ff71-341a-8fab-7c08455b9d41 | 1.2609 | -50.9344 | 2026-09-21 15:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 6f26624a-f107-3dce-bb19-5fa3ae7f13e1 | -10.4919 | -51.279 | 2026-09-21 15:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 8fb98929-1dd1-331b-949a-61737586b41f | -10.2979 | -50.2372 | 2026-09-21 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| d0ee9f57-80e1-306c-bfa7-0bbce5425733 | -6.306 | -55.9253 | 2026-09-21 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| baeb4b83-1832-3c60-93ac-9eb8d19af0d5 | -3.4555 | -50.5927 | 2026-09-21 15:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| cf28a573-86d9-3062-bfa7-a729ce161908 | -9.1147 | -65.9379 | 2026-09-21 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| cf350da4-4c5a-3285-bf9b-f521251f36d3 | -10.279 | -50.2391 | 2026-09-21 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |


[Clique aqui para ver as próximas entradas](README141.md)
