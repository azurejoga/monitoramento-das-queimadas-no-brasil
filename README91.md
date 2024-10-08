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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be194f15-b912-3cc1-9252-6d4ea6661c48 | -20.65199 | -45.92256 | 2024-10-08 04:59:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d53c0f6d-c38d-3b07-8f0a-33e7ea4d7c98 | -20.64826 | -45.91584 | 2024-10-08 04:59:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 72fceefd-ae59-31e4-9307-06eb3a2c73c2 | -20.64793 | -45.91961 | 2024-10-08 04:59:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e08bf109-bdbd-3f1d-b5c2-5f69dd0dfe26 | -20.64758 | -45.92368 | 2024-10-08 04:59:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 580680fa-d4d7-34d5-a0eb-a75f1de726c3 | -20.64721 | -45.92792 | 2024-10-08 04:59:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 996c8836-1eef-33e9-8155-77c4913c3058 | -20.64594 | -45.9222 | 2024-10-08 04:59:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d660f604-16ef-3b2c-87d2-4ccfda715aa3 | -20.64555 | -45.92628 | 2024-10-08 04:59:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f303d370-969d-32c8-98d1-b709c9c41175 | -20.64516 | -45.93044 | 2024-10-08 04:59:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d58a939e-3a30-327a-9522-32b43bd87139 | -20.64122 | -45.92671 | 2024-10-08 04:59:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ea5c69c-9e27-3380-8558-afe4b9592e94 | -19.866 | -45.68673 | 2024-10-08 04:59:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2934cb09-768a-39b3-85f0-f08f0f22223e | -19.85993 | -45.68614 | 2024-10-08 04:59:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc8e870d-67c5-3cfd-bed5-74b728c64c38 | -21.8215 | -45.6823 | 2024-10-08 04:59:00 | NPP-375D | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c4b7ecfd-8af2-3835-9876-d6743c0dfc00 | -21.81531 | -45.68163 | 2024-10-08 04:59:00 | NPP-375D | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 745618ca-9a00-35de-b59f-b44fed16d23e | -21.20111 | -45.79622 | 2024-10-08 04:59:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 60f32dd7-ced6-3777-b298-ad5c15273a71 | -21.20054 | -45.79697 | 2024-10-08 04:59:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 5e07665c-3a41-3582-be20-c1bec8543ad4 | -20.97838 | -46.08133 | 2024-10-08 04:59:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a1153546-be9d-36ec-8563-fb2e22b2e15d | -20.97795 | -46.08622 | 2024-10-08 04:59:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| eec8162a-bfec-30fd-a3e6-b8fc2bb69b73 | -17.78187 | -53.0794 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3223a1d-f0d4-33ac-be59-cafc8d66e7d7 | -16.59353 | -46.48756 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a483f7b3-9246-37d6-acfb-1866d03240fd | -16.5931 | -46.49139 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd412f99-32e7-305e-870f-8fbf87bdcc64 | -16.59292 | -46.48608 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95b58073-44ae-3c60-908c-4d2d12dc1dea | -16.59266 | -46.49525 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 720cbdd2-b8a2-3dd7-b4dc-b2ea0fb2138c | -16.59252 | -46.48989 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01c13e03-5a2b-385a-9027-6c1116ac6095 | -16.59222 | -46.49911 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b8d4955-72ea-3496-9674-ab14c5ca5d82 | -16.59211 | -46.49375 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| af141857-0634-3310-bbeb-3265731bb8f8 | -16.5917 | -46.49762 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8515c842-e571-3c32-bd24-63e21f7e5cff | -16.5884 | -46.48316 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 077d9af3-7a71-371f-b3fa-b14b78ce8412 | -16.58797 | -46.48695 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2b46a60-400d-343f-b65c-fcf23d3b243c | -16.58776 | -46.48166 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1daabb34-0c51-337b-b04e-a3cdaea6aca3 | -16.58754 | -46.49079 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbe782e5-5f95-3e1c-b55b-afb115396f75 | -16.58736 | -46.48545 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| efdbcc47-3716-3da1-8de8-950a0e7b3b40 | -16.58711 | -46.49464 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01329ca8-4e17-3810-9da1-0a8c83830cb9 | -16.58696 | -46.48928 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| daaea9f1-f5e2-39da-8123-d213f5e5ae79 | -16.58667 | -46.49848 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7a44d5f-fc4a-3a61-bf79-31f7d733474c | -16.58614 | -46.49698 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d0d7776-bee1-36e2-8c46-65b39ccd9551 | -16.58284 | -46.48254 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee1e0110-4d0b-3091-bec3-4743cf3f1db0 | -16.58241 | -46.48635 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d87af5c4-f469-3b2a-81bc-ea5a7f6e9f24 | -16.5695 | -46.45071 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 50c00633-c139-33fa-9a98-5f3c86ea3074 | -16.56908 | -46.45446 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 5ca88904-d6ea-3667-8b26-a757a0268d07 | -16.56866 | -46.45823 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 22b2b3b0-aa3a-32d5-a1fc-03af98e44e2f | -16.56824 | -46.46201 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| bec53351-38f6-3afb-8175-e04e2ab7e740 | -16.56391 | -46.45024 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f092c53b-5169-344c-b1e4-ff72b78e7448 | -16.56349 | -46.45401 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 6bc1abb8-bc52-3ed0-a329-ceddc7aa41b3 | -16.56308 | -46.45778 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 198cc7dd-665f-34db-b5f7-254c7059b6aa | -16.56266 | -46.46152 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| acafdf99-1cee-3b46-8a5c-a7c9900353ee | -16.56225 | -46.4652 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cb9ce516-72a8-3676-b155-e4e737df3bb1 | -16.5567 | -46.46451 | 2024-10-08 04:59:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b84c6d28-3e20-32a8-bafa-123a3551e05a | -16.88363 | -47.18546 | 2024-10-08 04:59:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 08648a3b-5a08-3325-a8be-86cafedf8e67 | -16.88327 | -47.18867 | 2024-10-08 04:59:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ded4bcdc-0bd0-3732-b636-8a3310f3e3b2 | -16.88292 | -47.19181 | 2024-10-08 04:59:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6d6c593-74c7-3667-89a5-c9a08b5f4b2d | -16.87829 | -47.18493 | 2024-10-08 04:59:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1c2f4a2-2920-3ff2-a168-64c6aaf0019f | -16.87794 | -47.18811 | 2024-10-08 04:59:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6bf55c7b-69af-306f-930e-38077d3f1cae | -16.87759 | -47.19126 | 2024-10-08 04:59:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8771517-9294-3eb9-ae63-b7e010166c5e | -16.87562 | -47.16032 | 2024-10-08 04:59:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f40bedb7-4cdb-3d2f-a2fc-beb3dbf3dffe | -16.87261 | -47.13859 | 2024-10-08 04:59:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 568be495-ce6a-36da-b287-5c32952aef22 | -16.87066 | -47.15626 | 2024-10-08 04:59:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18a82b1e-7d79-3d3b-8654-ffe5a65495b8 | -16.87028 | -47.1597 | 2024-10-08 04:59:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fed87ce-8687-30ab-9682-ef400f0300e3 | -19.46803 | -46.8445 | 2024-10-08 04:59:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b974dbee-6ea0-3435-8e28-8abf43528fc4 | -19.19592 | -46.58225 | 2024-10-08 04:59:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a66b1d68-40b6-3681-98bb-4b806cb40251 | -19.19553 | -46.58614 | 2024-10-08 04:59:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd0f5150-6899-36d4-8fcf-f9ebc8c728b7 | -18.72007 | -46.49022 | 2024-10-08 04:59:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef5f8b7f-4265-3bfc-8dbb-9f1f22dc6855 | -18.31299 | -47.16051 | 2024-10-08 04:59:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a2b2cfe-6608-318a-8230-236e154aa146 | -18.30758 | -47.15965 | 2024-10-08 04:59:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f409a06c-9d28-3cd7-9d99-e6df13ff9f37 | -18.29116 | -47.15098 | 2024-10-08 04:59:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| beed377e-0894-30a5-bd35-eeb0d236fe88 | -18.29082 | -47.15416 | 2024-10-08 04:59:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5d263c3-69ad-3ed2-88d0-4063dd2dc995 | -18.29045 | -47.15752 | 2024-10-08 04:59:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e680cff1-affd-3d7b-a167-12e0c3dfa114 | -18.28644 | -47.14369 | 2024-10-08 04:59:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50fdad57-df45-3c68-b4ef-826ab927eff8 | -18.28175 | -47.13622 | 2024-10-08 04:59:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d75f056-e982-3c09-ae74-26f92c397e21 | -18.28138 | -47.13965 | 2024-10-08 04:59:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e4543b1-b000-3376-b759-9e52f8fd8e48 | -18.28104 | -47.14281 | 2024-10-08 04:59:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c3ffed9-0c43-3ec4-9046-f5e906ea0d46 | -20.45588 | -47.62495 | 2024-10-08 04:59:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5170578-9470-3b1c-bc79-b0e52d01bc91 | -20.45552 | -47.62849 | 2024-10-08 04:59:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa06cff5-6a52-3100-8816-594c970b3fb3 | -20.4304 | -47.66052 | 2024-10-08 04:59:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b6c7ee6-9773-3d76-a85f-044b6f20ccde | -20.43005 | -47.66394 | 2024-10-08 04:59:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1e369ec-7690-3394-bd74-bee3900837a1 | -20.42969 | -47.66748 | 2024-10-08 04:59:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29355d38-0464-3ed5-b723-bf28ef8da041 | -20.42865 | -47.6778 | 2024-10-08 04:59:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10a7c249-efae-31d1-a4d7-b793ab6498cd | -20.4283 | -47.68124 | 2024-10-08 04:59:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32b4b94b-5648-3875-8286-9acd589bf0fc | -20.42674 | -47.64264 | 2024-10-08 04:59:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ae549f11-2961-3e10-af0a-aaf1a6b26aca | -20.42571 | -47.65282 | 2024-10-08 04:59:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16443e62-5191-3b02-b9b2-78df13c65a14 | -20.42537 | -47.65616 | 2024-10-08 04:59:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2f22ff7-6e75-3085-936d-dc342ada470d | -20.42504 | -47.65953 | 2024-10-08 04:59:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17795e16-12b3-3d13-84df-9401df3da3d4 | -20.42469 | -47.66296 | 2024-10-08 04:59:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eb3a6e0e-866b-383e-b26d-988cfe208fbf | -20.42433 | -47.66654 | 2024-10-08 04:59:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2bb82132-ce19-3dc3-bf0d-35faee59abc1 | -20.42396 | -47.67016 | 2024-10-08 04:59:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50788b37-faee-34d8-9f63-54d50745c043 | -20.4236 | -47.67374 | 2024-10-08 04:59:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de7c8d75-abe7-3626-8dd1-46e2c5339661 | -20.42288 | -47.68087 | 2024-10-08 04:59:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76b3e129-17eb-3988-ad17-f62bff391715 | -20.42173 | -47.63813 | 2024-10-08 04:59:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa962d81-81ac-3750-bbb3-f4f5af1b2312 | -20.42139 | -47.64151 | 2024-10-08 04:59:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4ea39004-8a46-3045-a4bd-44b6b598cb8f | -20.42105 | -47.6449 | 2024-10-08 04:59:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb91006e-ee3a-332b-9996-8249dcce39e2 | -20.4207 | -47.64832 | 2024-10-08 04:59:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 23b622ba-527d-33e0-8fed-4db8d270a684 | -20.42035 | -47.65177 | 2024-10-08 04:59:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 289be83f-3954-30cc-8b54-952a851283a6 | -20.42001 | -47.65524 | 2024-10-08 04:59:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 547c3b5f-5cf2-31f5-a19f-ee474ee4e7c3 | -20.4193 | -47.66231 | 2024-10-08 04:59:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ea6dba3-dcda-3303-9d70-87ceb5d9845c | -20.41893 | -47.66599 | 2024-10-08 04:59:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ee4cb37-96c7-3b2f-bebe-4743e03e5d6e | -20.41855 | -47.66971 | 2024-10-08 04:59:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a47bec92-a45e-3d5c-9414-c484d206d902 | -20.38642 | -47.04542 | 2024-10-08 04:59:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 94861ebf-65dd-34d1-aed9-893f2218b42a | -20.386 | -47.04969 | 2024-10-08 04:59:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86f9d92a-36db-36d6-a026-24bb70a5b81c | -19.81793 | -47.39453 | 2024-10-08 04:59:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ed22930-076b-3b8f-9654-32e38f7bcc45 | -21.60299 | -47.71812 | 2024-10-08 04:59:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7b97792-c7ed-35a4-8f2c-b1618dd3a8f3 | -21.59782 | -47.71463 | 2024-10-08 04:59:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README92.md)
