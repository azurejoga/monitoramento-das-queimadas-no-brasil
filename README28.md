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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ea006be-6f26-3a36-841f-b01ffbbf3e2b | -7.08152 | -42.12025 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 259a5243-ca1d-3995-b668-8bb26400932f | -9.36171 | -50.09793 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e1e83856-484b-3e81-9261-02ff10dd7f36 | -11.49149 | -45.75087 | 2026-09-15 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f78f825e-b2c2-30f2-b226-74262a502ec0 | -10.50664 | -53.57187 | 2026-09-15 04:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8c6f1a7-13f9-38db-8fbe-ec7db19ffca3 | -7.08836 | -41.82317 | 2026-09-15 04:14:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 57620563-d624-398d-8ee2-be369cc4ffc2 | -11.24848 | -43.45142 | 2026-09-15 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a74c70ca-29e7-3e8d-88c9-77843c961d4e | -11.1758 | -42.79251 | 2026-09-15 04:14:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1883c1e0-2ee4-3466-ac92-8afbcfc9369f | -10.69862 | -47.5022 | 2026-09-15 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d7a4184-88f2-3a80-9474-73c255517305 | -10.66654 | -54.1411 | 2026-09-15 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 79907279-0b91-3b44-b0cc-84d1dfc151ac | -6.95229 | -44.5389 | 2026-09-15 04:14:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1453f659-766c-3a1e-b1ca-d70964f22eea | -11.19136 | -42.82122 | 2026-09-15 04:14:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 889241c4-bdb5-335d-a3f1-c375f1256aa3 | -7.48028 | -42.12164 | 2026-09-15 04:14:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 41334759-04a3-3225-9fc4-582d7b4dd81d | -13.6214 | -42.44767 | 2026-09-15 04:14:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e17ccf60-9c41-31e4-a633-38b474d46466 | -7.07994 | -42.10836 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 954f77d0-cb71-377a-a587-b911ce9ca72b | -7.10497 | -41.80706 | 2026-09-15 04:14:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 27bab4e4-e7a8-31a3-8486-817f847d2a42 | -7.54687 | -46.86923 | 2026-09-15 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e3659a6-29fe-3cf0-8871-9f77684c76fa | -10.06632 | -45.48455 | 2026-09-15 04:14:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23ee49af-aead-36b6-942b-7d31f70e9311 | -11.24937 | -43.46768 | 2026-09-15 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f1deac15-2571-3ee6-a400-45be2d97a0ee | -9.36035 | -50.0981 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2a2af3f-bb65-3512-95f3-a1140510f6cb | -7.09252 | -45.04141 | 2026-09-15 04:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| caaabe2c-1720-3542-94e2-6a568326331c | -11.81125 | -46.5851 | 2026-09-15 04:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 894d22da-104d-347a-be60-5b1a9a04d436 | -7.16959 | -43.51923 | 2026-09-15 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2b5651f3-032e-3a24-ad6d-c7bdf3386d50 | -7.16283 | -42.09882 | 2026-09-15 04:14:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fa410a14-5a43-316b-b5d3-1bd41aa6ab6e | -8.09703 | -43.77974 | 2026-09-15 04:14:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f79735d1-b473-3166-82f3-638712acdb79 | -12.8541 | -44.3916 | 2026-09-15 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3c4f74e3-2468-39bb-8341-fe4c0143158c | -9.02221 | -47.74808 | 2026-09-15 04:14:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e50e53b7-3d30-37e6-8030-f3659d84a774 | -11.33452 | -46.78644 | 2026-09-15 04:14:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a641439e-7f97-3b98-b9af-843ad66a45a7 | -8.63602 | -44.45118 | 2026-09-15 04:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2bcdcec4-9739-3a6c-ada2-27fc9a083ddc | -11.25197 | -43.45201 | 2026-09-15 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7381eb7e-b52e-3b91-a968-df31919e4c67 | -11.17249 | -46.38086 | 2026-09-15 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abc4b15d-325b-3635-926c-4571b8c7cd92 | -11.47472 | -47.43993 | 2026-09-15 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 97a0e5c5-cb49-3469-9536-8a2f1257872d | -7.10851 | -47.4812 | 2026-09-15 04:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c69c6b16-e401-32d3-b58d-cdfbeb643a7d | -11.24279 | -43.44239 | 2026-09-15 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25056056-2439-3a48-9e47-0f9a5cf00606 | -7.10308 | -42.09671 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 80c9c2f5-11b1-398e-87c3-0384a16cca71 | -11.23473 | -43.4692 | 2026-09-15 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 92900a0f-a699-32e7-9119-f3f47b57ee1f | -8.2602 | -47.98153 | 2026-09-15 04:14:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 74941cc3-dcd6-3323-8d3e-e3d52fc85739 | -9.35971 | -50.10157 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 81694bb9-7d51-3195-89a6-498882a88b9a | -7.16245 | -43.52454 | 2026-09-15 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ef180a61-c0a4-33c1-bf6b-82bc17da3cff | -6.14893 | -43.81598 | 2026-09-15 04:14:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0dbb9494-cb45-3802-bd1e-f22495e47abf | -7.01806 | -44.62231 | 2026-09-15 04:14:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fefeca0-d2d1-32b8-a248-9456aa41a53f | -7.96603 | -43.97907 | 2026-09-15 04:14:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25397dd8-f20b-3f0b-a7e0-678b1c2a252c | -9.25659 | -48.54727 | 2026-09-15 04:14:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b95aed1-b8f8-3cc5-be05-b2c7e833ff28 | -7.16519 | -43.52293 | 2026-09-15 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fc3d0995-b8ba-3b6b-9eed-6094fa3db618 | -10.65981 | -54.13948 | 2026-09-15 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c447c467-c32e-3290-b838-9cc69ef53c95 | -7.08373 | -42.12834 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4a0f936a-16fc-3c83-86f7-0e55c57da3e9 | -7.09901 | -42.09991 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| baf6f395-a3b8-358a-aa4a-19cdbb23e2e1 | -8.80753 | -46.91096 | 2026-09-15 04:14:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd465ea6-4f77-3444-9c3e-3a31d774a8ba | -10.67627 | -54.16264 | 2026-09-15 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0ba2dad-3ac3-3d2e-9003-b8e3c0903097 | -11.17739 | -42.80428 | 2026-09-15 04:14:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c0db4adb-3103-3a82-884d-37e07599625c | -7.10156 | -41.80649 | 2026-09-15 04:14:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5cc52527-413e-3bc7-95a4-981e3725d936 | -8.48693 | -44.58469 | 2026-09-15 04:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8666ffb7-cf89-35a1-8b11-1062b9f34592 | -7.22807 | -46.15527 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59161b3b-7407-3df0-add1-3d9c99153f99 | -7.61469 | -47.29673 | 2026-09-15 04:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06f739ca-cadc-3cf2-8476-faa4629c4ad3 | -7.16814 | -43.52782 | 2026-09-15 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 86ea1a8b-5e29-3b47-80eb-888cd554c429 | -5.31226 | -49.25726 | 2026-09-15 04:14:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 843f69f4-f46d-3c57-abc0-291a721bc279 | -9.35332 | -50.13655 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ebd7114f-0409-30df-9af3-cc40ad38b4fd | -8.5082 | -50.14912 | 2026-09-15 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9ba882d-d538-3168-bb32-94af6a16e490 | -8.63522 | -44.45582 | 2026-09-15 04:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e1225ab-673f-3426-b8dc-30643d745ae1 | -13.55288 | -43.53183 | 2026-09-15 04:14:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a08c2abd-9865-3433-a5c3-a0f8ad45eb95 | -7.16613 | -43.52513 | 2026-09-15 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 8556745e-a937-321e-842d-43295d4cb017 | -6.78511 | -39.21994 | 2026-09-15 04:14:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2e5403aa-891d-3609-aa65-48bce5c65cc5 | -7.09638 | -41.81693 | 2026-09-15 04:14:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b24ae955-b3bf-33a1-a525-6ffe0bd8d775 | -6.42704 | -43.06857 | 2026-09-15 04:14:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dfc5dd59-8885-3677-b5b1-bc569c7b0f19 | -11.22905 | -43.46017 | 2026-09-15 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23db81a6-7b95-3b52-9d74-ddccf8994b8c | -9.42795 | -49.54847 | 2026-09-15 04:14:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fe9916d-855d-36be-84c7-5d8436bcb373 | -7.23391 | -46.17315 | 2026-09-15 04:14:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2a299e2e-bbda-304f-aaef-fa08d3b39a77 | -8.80057 | -50.49341 | 2026-09-15 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a728b382-57f7-3387-a5da-da17442b5cc3 | -7.4421 | -45.48262 | 2026-09-15 04:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c0fad10-e63e-3701-9b0c-080999ed85b9 | -9.85207 | -48.34739 | 2026-09-15 04:14:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 061f9390-7b79-34be-8b90-310ff9b8addc | -7.24956 | -46.15931 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 92ae3bf1-de1f-31e2-b18f-2fce4b677d60 | -7.10714 | -42.09351 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| fbc44f43-a808-3c16-a947-6279734b25b4 | -11.49238 | -45.7458 | 2026-09-15 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ef23bf0d-2f66-37ff-8213-c4f22c68ea7b | -9.35461 | -50.1295 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53641a36-6d46-3e8f-9806-e0d47ccaf320 | -9.35773 | -50.11881 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31950ad6-8e9e-3acb-a059-7fb9746be6d2 | -10.03644 | -52.09301 | 2026-09-15 04:14:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 178f66ae-4da5-3aaf-bfca-14c62192ba1a | -6.15695 | -52.74065 | 2026-09-15 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e8904d2-53e2-3c02-bf6b-6ab6ad4d8fbf | -12.49195 | -41.42081 | 2026-09-15 04:14:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0e725550-2154-32fb-8a19-05653cc33a96 | -11.21136 | -43.437 | 2026-09-15 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4805f21d-686c-32a5-9da8-d4e8b720c867 | -6.52057 | -44.02315 | 2026-09-15 04:14:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f529d78-6909-3a4f-b817-672559e45d8b | -7.2246 | -46.17565 | 2026-09-15 04:14:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 912c9ddb-e88e-39e7-bb1c-1a9e68b45699 | -7.23099 | -46.16416 | 2026-09-15 04:14:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8394c29-6994-38de-8709-18ad5ba6ee59 | -8.50366 | -50.1463 | 2026-09-15 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 11b86e8b-148f-3cef-b48f-85780243b56b | -13.30599 | -43.7156 | 2026-09-15 04:14:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9acbad7-9ff3-3e66-b17f-f9096937bc53 | -9.31881 | -44.3505 | 2026-09-15 04:14:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cf7a85f-8827-3982-aaf6-2beb36197fef | -11.33108 | -46.78141 | 2026-09-15 04:14:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08314c54-7fb1-305c-b975-5f8f0566ef78 | -11.81948 | -46.58651 | 2026-09-15 04:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a05e151f-99ae-3e89-8f3b-309f1eeab362 | -7.24654 | -39.27782 | 2026-09-15 04:14:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 39971732-7d6f-3352-8ded-d4b21b349122 | -8.48473 | -44.57433 | 2026-09-15 04:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e90c8e33-cce9-38f6-ac40-e3a2ee115635 | -7.93292 | -49.73569 | 2026-09-15 04:14:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9170f116-4143-3e91-99c4-f3c512891f41 | -6.30061 | -41.68305 | 2026-09-15 04:14:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9454ff88-46f6-3bfa-94b6-35310f772cce | -9.87461 | -47.78262 | 2026-09-15 04:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fb80e984-df14-3a32-aff2-e5fc722d6a78 | -6.67722 | -46.19518 | 2026-09-15 04:14:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77726f89-1cbd-3a0f-945c-ffdb7e24fb1f | -9.35519 | -50.188 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6026bc9-7aa2-3d1e-91b9-60935f3b21ef | -11.4958 | -45.77251 | 2026-09-15 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e27d96d-da49-38ca-9814-cbc7905f3b64 | -12.3205 | -41.78066 | 2026-09-15 04:14:00 | NPP-375D | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 87503e62-7c26-34f7-ae50-9d93b336b2c4 | -9.35717 | -50.11552 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57374c7e-9e7c-33be-a57e-4bfc3b2374da | -11.98243 | -52.47035 | 2026-09-15 04:14:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb4d3103-1a9a-3506-baf6-1d4d9e9dcee2 | -8.59672 | -44.47997 | 2026-09-15 04:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e3b4db8-ee8b-31a2-91d3-e94eae000664 | -9.35583 | -50.18447 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 98eb0bae-63af-30a7-b4da-721de4315d38 | -9.35829 | -50.08644 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |


[Clique aqui para ver as próximas entradas](README29.md)
