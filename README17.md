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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0be83bc8-c921-3241-ab23-8cd367c7aacb | -5.39217 | -40.66383 | 2024-12-13 04:21:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ad378157-57e7-32d6-92ef-03c262d50f47 | -8.27379 | -48.02673 | 2024-12-13 04:21:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f1191e0-6524-3a38-92be-51b972bb85be | -6.05845 | -44.04219 | 2024-12-13 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 340d6bd5-7871-3162-9e85-72df53c4834a | -5.62944 | -45.38881 | 2024-12-13 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c364c55d-8332-3ae8-a1a4-300c97181535 | -10.03031 | -36.28754 | 2024-12-13 04:21:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d3e16bd2-9c72-37dd-b0ad-d6d7bd07cb7c | -2.23174 | -53.72747 | 2024-12-13 04:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2af2ac2-38c8-36fa-b96f-ce485084602b | -6.0579 | -44.04569 | 2024-12-13 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| bcd1561c-8d04-3142-a4e8-60ab1ea6e878 | -10.21629 | -47.58104 | 2024-12-13 04:21:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 628fb353-c87c-3b08-b33a-122b9aa5e52d | -4.91326 | -37.48798 | 2024-12-13 04:21:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 017abfd9-213c-37a6-a3ab-a5de0cd4c317 | -6.28248 | -49.64566 | 2024-12-13 04:21:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 735e9527-965b-3a03-804f-aca93d4d93f1 | -5.95622 | -39.67926 | 2024-12-13 04:21:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 98f3376d-83b4-35a2-8b10-1a18ab085ab7 | -3.47534 | -45.79643 | 2024-12-13 04:21:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30312a5b-c223-3ec5-8e36-1168cf1c144c | -9.16358 | -49.48108 | 2024-12-13 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 525bebae-f292-3f2a-8448-4a8f7af6a9ca | -5.62923 | -44.83862 | 2024-12-13 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bdfe2762-d3e1-3f42-a3e6-e3a85048fe26 | -7.83347 | -35.18094 | 2024-12-13 04:21:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 55041496-645e-37d7-8cb7-67a4e6ca470b | -10.02988 | -36.29087 | 2024-12-13 04:21:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7c3260c6-1f06-33ef-b8b3-c8a818a7970e | -7.97207 | -48.16047 | 2024-12-13 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dc409d3-9454-36ba-8dcf-d5721d716f19 | -10.02531 | -36.28389 | 2024-12-13 04:21:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| e1f2ab57-897e-3ae2-997e-558c8156ec11 | -2.80844 | -53.0691 | 2024-12-13 04:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 37e6354e-225c-3a18-8f79-d28d6d520edf | -3.28709 | -45.59554 | 2024-12-13 04:21:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c03efff6-f3b1-3381-aa2e-c660be4e06d8 | -5.2109 | -43.29798 | 2024-12-13 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 1460236e-075c-36f1-b1bf-a44cba623c9c | -6.21842 | -43.95226 | 2024-12-13 04:21:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5cd3df1a-1228-338e-855b-081699a3c064 | -2.81325 | -53.07335 | 2024-12-13 04:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e693b007-6eb4-3a2d-a1db-cb6205a31b03 | -4.17841 | -42.43814 | 2024-12-13 04:21:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2af1d780-5b9d-344d-b570-42fabc2c107b | -10.02445 | -36.29045 | 2024-12-13 04:21:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| d0335aa5-9b62-35af-a7b0-ca6c76c272a3 | -5.20754 | -43.29745 | 2024-12-13 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 3ac939e1-af11-3598-a91c-9a62d93335d9 | -4.55211 | -43.57897 | 2024-12-13 04:21:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bf27107-43a3-372f-9195-3c26f22e2c26 | -3.77182 | -50.69641 | 2024-12-13 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0174bef8-9d81-3aff-873d-58b091b66055 | -6.32125 | -44.76348 | 2024-12-13 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fdd6a718-5a53-3428-8381-1e9e5a407b71 | -4.16644 | -42.4476 | 2024-12-13 04:21:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d37f647c-9a75-3862-b346-fccba6ff4ffb | -6.11656 | -43.95443 | 2024-12-13 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d69f19bf-4044-366b-b537-c8686777898d | -2.91446 | -48.02914 | 2024-12-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56b51a28-0a7e-3048-b81d-82fdd9006631 | -4.77178 | -44.41951 | 2024-12-13 04:21:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdd78fd8-6433-38a3-9a07-e6b356eab744 | -7.97428 | -48.16938 | 2024-12-13 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8b6065a-cb24-3408-af01-6b5ea23b6b08 | -3.10408 | -48.27964 | 2024-12-13 04:21:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c58539d-6b53-34f5-ac5f-44c9f20a7270 | -4.13562 | -50.4163 | 2024-12-13 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c47b7b75-105a-39c4-bd9d-55fc0134c842 | -2.22672 | -53.72271 | 2024-12-13 04:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fee3fa2-74ef-364b-ad94-986b3b922eab | -5.45454 | -44.81126 | 2024-12-13 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e719417b-99af-3a6d-bb81-f9fd16deaad3 | -2.8138 | -53.06998 | 2024-12-13 04:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fad99e6-e8a7-306b-9fda-9c44a7cb6e23 | -3.83302 | -41.57226 | 2024-12-13 04:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2d2539a6-d5b3-3931-b94d-35568c669018 | -10.66403 | -44.71692 | 2024-12-13 04:21:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ff71d35f-77d8-36fd-80c4-844820527488 | -9.19948 | -49.47766 | 2024-12-13 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| af759e15-a961-3f1a-9e89-67b8dd3fe5cc | -5.45841 | -44.80832 | 2024-12-13 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd3e0bc1-5b71-3026-9a1b-1335e99f310c | -5.63255 | -44.83914 | 2024-12-13 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a1ed20fe-052e-38bc-bfc5-4ba95d3198c8 | -4.16758 | -42.44024 | 2024-12-13 04:21:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| fbba0aca-a4b9-3725-98b5-e7831ce7240f | -3.26899 | -46.91738 | 2024-12-13 04:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aac6316e-c06d-373a-ad2c-3deb76aef1d2 | -4.52065 | -42.07154 | 2024-12-13 04:21:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bcc24002-7991-3fef-a9a5-5d8ecc8072b9 | -4.88257 | -44.40496 | 2024-12-13 04:21:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5db689a-89fe-30da-9dda-f9d36fe6267f | -7.25385 | -48.4184 | 2024-12-13 04:21:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7335d3c-d854-3d44-83f8-ee8191daf829 | -5.28902 | -44.91315 | 2024-12-13 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1791998f-3d88-35a1-a59d-ab00adfa2b18 | -3.29107 | -45.59245 | 2024-12-13 04:21:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c0484c30-7717-3a0a-9cb2-e64af16dcecb | -10.52612 | -47.8144 | 2024-12-13 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 066e40d1-ddac-3f91-955e-73fc1111ee60 | -10.23149 | -49.48246 | 2024-12-13 04:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20015515-c834-3445-a79e-60760f478e03 | -8.26664 | -48.0256 | 2024-12-13 04:21:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ebcb93f8-7019-3116-b991-d05feefaeccd | -4.43004 | -44.13966 | 2024-12-13 04:21:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 510cf9b0-053a-30a6-a84a-52bd1f4f5267 | -3.32232 | -45.70522 | 2024-12-13 04:21:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bb919d7-6813-3688-87c5-e01a891f52fc | -6.37841 | -39.25307 | 2024-12-13 04:21:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 45aa7d32-f56b-3737-b3d1-3d5e7570f6ea | -5.37857 | -43.50132 | 2024-12-13 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5a044b2e-d4c4-3387-a466-afb3437a73ff | -4.96965 | -44.96601 | 2024-12-13 04:21:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ebaa528a-be74-3523-953b-ee5f32d7fb53 | -3.66656 | -45.22853 | 2024-12-13 04:21:00 | NPP-375D | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f3131c4-e6eb-308c-9362-b30db47bcf79 | -6.08778 | -43.53493 | 2024-12-13 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98bd810d-ffa2-3613-a226-3d3cbf008217 | -3.15356 | -49.90583 | 2024-12-13 04:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2a3498d-4eb8-3fcb-ad94-05aaf79ffa84 | -2.00621 | -54.5121 | 2024-12-13 04:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb8197f0-2a3b-3c33-ac33-e45d56668925 | -9.28889 | -39.27359 | 2024-12-13 04:21:00 | NPP-375D | CHORROCHÓ | BAHIA | Brasil | 2907707 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8eabd2d1-5a00-31a7-a6b6-b1b959b1667b | -6.76814 | -44.82698 | 2024-12-13 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 91ffac7c-0e70-3fd9-ac12-4b593ffd6144 | -2.18925 | -53.65122 | 2024-12-13 04:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcdb3051-3439-30b0-a6a3-85c517e7cea3 | -6.76427 | -44.82993 | 2024-12-13 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 79e9c6b7-08b5-3da0-8667-66223385c30a | -2.91657 | -48.00794 | 2024-12-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed165342-fa53-3d1d-8ae0-66c113345331 | -5.05456 | -44.23376 | 2024-12-13 04:21:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 000d7cf1-5ae6-3c3f-9dc1-33c2c4dc1c6b | -8.00911 | -45.64125 | 2024-12-13 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c45d1afa-b300-39fb-ba68-de8a81d82089 | -5.65097 | -43.36208 | 2024-12-13 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bfe69fae-5beb-389b-97b1-99a7a0dc5e29 | -7.35943 | -46.23481 | 2024-12-13 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a011d9e7-0a84-3099-90bb-81a492ec3fb0 | -3.77102 | -42.25299 | 2024-12-13 04:21:00 | NPP-375D | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e6ffa66d-c010-325a-aac6-069cd38394a9 | -7.28863 | -45.08368 | 2024-12-13 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4db06a00-a777-3bfe-9ce8-9c2390ad6190 | -9.16989 | -49.47509 | 2024-12-13 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| baf5848f-0e12-3405-96e0-95ff81e536fc | -5.24034 | -45.13393 | 2024-12-13 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82a0aef0-b8a3-3fd0-b992-5224895dfbe8 | -4.81079 | -44.47166 | 2024-12-13 04:21:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1c381a9-3bfc-37da-b39a-65b830ede9e2 | -5.45235 | -44.82512 | 2024-12-13 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca5f95f0-38cd-310e-85c5-8978047874e2 | -3.10716 | -48.28506 | 2024-12-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cc401a6e-3bb7-33e0-80f1-053a74867707 | -7.43807 | -44.74034 | 2024-12-13 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e27c87b-a804-361b-bd24-9b9742c1ac3a | -2.50346 | -51.8069 | 2024-12-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7725580f-2120-3634-b162-6618f681a5ad | -4.25051 | -41.92641 | 2024-12-13 04:21:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f920e5f5-9414-3f2e-aabc-8f31863cab91 | -6.11322 | -43.95392 | 2024-12-13 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3293e044-95da-3f12-b3fe-b440d67e3419 | -5.44825 | -45.40369 | 2024-12-13 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fc4a822-b651-3001-9acd-1055c159e390 | -4.47924 | -48.1153 | 2024-12-13 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a89f37e6-e7f9-3c30-9a31-bcf91e02af09 | -9.72785 | -48.03051 | 2024-12-13 04:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be58849a-15b6-3221-a403-6b12a3f8a839 | -2.23803 | -53.72456 | 2024-12-13 04:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5078142a-e488-3296-8dc1-6163db16f05b | -6.73754 | -38.15942 | 2024-12-13 04:21:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 219b50ac-d252-3324-895e-81d1d6f15571 | -7.27575 | -46.1663 | 2024-12-13 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87970937-4893-3cee-8de6-4a0310ba9e6e | -1.99958 | -54.51506 | 2024-12-13 04:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6d6ae55c-a340-36fa-b8a8-e50d13be74c1 | -4.53513 | -43.29229 | 2024-12-13 04:21:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 202b774e-f9e1-3096-9109-0a65b4d38efd | -6.11267 | -43.95742 | 2024-12-13 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b1810b6-28bf-35f9-a43e-d460aaf2f421 | -9.17281 | -49.47305 | 2024-12-13 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1f6df959-4f48-3ba2-bf55-0c9db9af257c | -5.45509 | -44.80779 | 2024-12-13 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c512f4e5-1716-3d55-8b32-289c922a2e61 | -3.29049 | -45.59608 | 2024-12-13 04:21:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5b829507-0524-35cf-a497-bf54566cb018 | -5.9428 | -43.76897 | 2024-12-13 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c822fc53-9d6d-3d3c-8e02-8f03ca24f0f9 | -4.55139 | -48.00521 | 2024-12-13 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6e139e9-9887-3072-8b4d-3ecf36854893 | -9.13625 | -49.48862 | 2024-12-13 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 054b29c5-6cf2-3630-a4aa-1ec62a6269d6 | -10.03157 | -36.27802 | 2024-12-13 04:21:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2aa588c4-7236-3d36-bdbd-d4458658ce42 | -2.69919 | -51.64511 | 2024-12-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README18.md)
