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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70d81f1f-6e4e-39c1-9a20-97d0ed83d9e5 | -12.34968 | -57.42912 | 2025-06-11 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14a773b3-e456-332c-bf65-6869a0d43693 | -13.08941 | -47.43407 | 2025-06-11 04:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0241be0d-0fa9-3c4b-bb51-b553b76d33c8 | -11.56591 | -47.4337 | 2025-06-11 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d762a44-8ff5-3a3a-8806-7e142f949e64 | -10.36354 | -57.23866 | 2025-06-11 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3d81b03-7c3a-3d49-a2d9-94d22a0b15f2 | -10.18561 | -49.59975 | 2025-06-11 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee049031-d809-3eea-986d-2a4474ad87ac | -10.50525 | -53.58081 | 2025-06-11 04:49:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5e458c7d-9e00-3849-af27-9f78f081cda6 | -10.37324 | -49.86026 | 2025-06-11 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe933366-e2b7-30e7-af4d-97faf738ada2 | -11.36806 | -56.56277 | 2025-06-11 04:49:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4032551-894c-3400-814f-170b66c1309f | -13.09299 | -52.28733 | 2025-06-11 04:49:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07c06aa8-7bf0-3f1f-8461-cf5806067053 | -10.51097 | -53.63035 | 2025-06-11 04:49:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95ff3d69-47c2-3057-98ce-37e2aaab3d88 | -10.19318 | -49.59694 | 2025-06-11 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 57dc9e4e-5f45-37f3-b32d-2e187e0e28dd | -10.18794 | -49.58415 | 2025-06-11 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21da98b1-7010-34ac-99ee-dd2e9026a019 | -12.10557 | -49.48573 | 2025-06-11 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 40ee59df-f680-3d9c-88de-92187e56233c | -10.84873 | -53.78847 | 2025-06-11 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38270422-4c97-3ac4-aab3-7045583b879e | -12.52221 | -57.21312 | 2025-06-11 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a43bd743-ace9-35b3-ae3f-9db472ba0aa7 | -10.88328 | -54.75766 | 2025-06-11 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ec9a8d0-162a-324f-8a1d-eb834539e138 | -10.19435 | -49.58913 | 2025-06-11 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fadea363-7cb9-3006-adf0-7e7e6dbe7bde | -8.89906 | -49.10611 | 2025-06-11 04:49:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca8b878e-ddcd-3e88-b6aa-2086e1dbef19 | -11.88195 | -56.41256 | 2025-06-11 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ca214c8-e311-3cc9-ac38-0f3737f8976f | -12.20749 | -49.62534 | 2025-06-11 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86cc9523-48e6-350d-a1c2-5a65139192d3 | -10.87643 | -49.55079 | 2025-06-11 04:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab588c82-2b4f-3a26-8245-6b25a14fc4b8 | -11.62762 | -47.68308 | 2025-06-11 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 649b1db7-e681-34ac-ba4d-ff4a9e8851e0 | -10.88463 | -54.74961 | 2025-06-11 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28c73aef-d4cb-3911-929a-b51d999a5bcb | -10.8811 | -54.74902 | 2025-06-11 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 834bdea8-3bbb-3d97-a978-e38290884399 | -10.18911 | -49.6003 | 2025-06-11 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c169d2c-3056-36c5-aae5-156231291484 | -10.84313 | -53.77987 | 2025-06-11 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5587fa63-cd7b-32a3-b707-fd96b7d6e732 | -10.06107 | -45.35617 | 2025-06-11 04:49:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 675ed1b7-93de-3b3a-a3f9-e700370855d2 | -11.7642 | -55.57916 | 2025-06-11 04:49:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d96a89c1-538b-38f0-8d09-6870b2cc20a1 | -13.66731 | -52.19692 | 2025-06-11 04:49:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4d98dbed-238f-3d4c-a230-2a61e1b73427 | -9.18034 | -49.66896 | 2025-06-11 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ba3791f-faac-3df8-be74-185e716cdd4c | -11.5899 | -51.34292 | 2025-06-11 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb37461b-8f16-338d-8ca9-6c46eed7d294 | -12.2081 | -49.62127 | 2025-06-11 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37f74ac7-8d0b-32dc-8c44-7725224683bc | -14.25488 | -45.49551 | 2025-06-11 04:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6fe94bf1-78b3-3118-8ff2-070fe8e7eae9 | -14.25082 | -45.48979 | 2025-06-11 04:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6338a9b7-de84-3de7-8898-1cfbbd841f8c | -12.52131 | -57.21819 | 2025-06-11 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a09445cc-d3ac-3664-9562-67cab4ccba33 | -12.28062 | -57.27457 | 2025-06-11 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc2eb8b4-2718-35ed-bc65-5d1d4a06fe9a | -12.19923 | -54.26773 | 2025-06-11 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 551cbbfa-ef3f-3333-a6c3-29ebe707a7f8 | -8.96206 | -47.96595 | 2025-06-11 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 90d6f88e-dc54-37ff-ab88-a62c33da1966 | -11.04832 | -55.04263 | 2025-06-11 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbbe5f14-29df-3da6-83e0-bffad57f57a3 | -10.36402 | -57.50345 | 2025-06-11 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3bec4c98-bf76-3175-a96d-e8f07b6ed1b7 | -12.21271 | -49.62891 | 2025-06-11 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c08fae48-08f1-3db3-a157-510360072123 | -11.58599 | -51.34597 | 2025-06-11 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4663ccc5-cfcc-34c6-be4e-20e34c1a5d80 | -10.18969 | -49.5964 | 2025-06-11 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f84c56d0-affb-3122-af54-91433e0cc028 | -10.36763 | -57.23933 | 2025-06-11 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea1c7fc9-bd2b-3437-b058-ca782e1abf65 | -10.24123 | -52.22435 | 2025-06-11 04:49:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 600e1eeb-75b1-3175-bedb-70af539f6cf7 | -11.77287 | -54.37696 | 2025-06-11 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adf4478e-d9e9-3fca-ba0c-f3a24807f92a | -10.23568 | -52.23786 | 2025-06-11 04:49:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa3dc7c1-1037-393e-bdc8-b40c9938f554 | -10.69789 | -49.51777 | 2025-06-11 04:49:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e2558a45-c5b1-356f-9d0b-90cb386048b7 | -8.69606 | -49.84572 | 2025-06-11 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84d6e210-4f61-3f98-ac1e-dc67a9adf3c8 | -10.05102 | -48.66981 | 2025-06-11 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a9f297c-2655-37a8-9eb2-76df261bc095 | -12.13483 | -54.65812 | 2025-06-11 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4da9403-73ae-3cc0-b011-208280474b86 | -11.77632 | -54.37756 | 2025-06-11 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ff3364c-1b9e-3cd5-b2f6-dd0ae00e0b15 | -12.52797 | -57.20358 | 2025-06-11 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d54fae0-0804-3963-a263-0ce92bb658f5 | -10.64979 | -49.42907 | 2025-06-11 04:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a712a3b9-62e4-3f39-8d3b-0ff6d7220e36 | -11.6263 | -47.68522 | 2025-06-11 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf4ceb92-90e6-30cb-be7e-fbc2b0649941 | -11.6269 | -47.68804 | 2025-06-11 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 423619ce-9a59-3775-83a0-bc4f7d5a48da | -11.88521 | -56.41058 | 2025-06-11 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ec6212e-3cc1-3707-9119-e8b06b677692 | -11.8323 | -51.28556 | 2025-06-11 04:49:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93c43694-850d-35f3-ba2b-d706e3bc826b | -11.34041 | -45.21692 | 2025-06-11 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2a85b702-425a-37d1-a07a-88d9f323b9ac | -12.29394 | -50.10617 | 2025-06-11 04:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3ce9ec0-e7e8-3936-bc13-59b333c8310b | -10.239 | -52.2384 | 2025-06-11 04:49:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 55780b78-8545-3de3-8678-9a21f937a928 | -9.8185 | -61.40568 | 2025-06-11 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6ae0aa8-2e3b-38c6-810a-9e485dd7442f | -12.78717 | -48.72782 | 2025-06-11 04:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a1708594-e704-3912-b6db-a5ac5e0d8fe5 | -12.2678 | -47.0074 | 2025-06-11 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22ddab0e-366e-3ab0-8f88-e7d84d07b082 | -10.50696 | -53.63347 | 2025-06-11 04:49:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae7105e5-0bfc-3673-9bf7-2aa2755e12e0 | -12.52403 | -57.20287 | 2025-06-11 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6305170-6eab-33cd-9c3e-ba940f65aa80 | -9.78087 | -57.42702 | 2025-06-11 04:49:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0764012-3428-324e-8209-52031004fa5e | -10.07283 | -52.75075 | 2025-06-11 04:49:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a5f2b5c-8868-3793-ba29-ce36f1572429 | -10.18619 | -49.59586 | 2025-06-11 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b6ba160e-4ace-3d44-91de-0e30621e58f2 | -10.65333 | -49.42962 | 2025-06-11 04:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0beb137b-150e-3ca2-99c6-1907c60d4f23 | -10.70493 | -49.51886 | 2025-06-11 04:49:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2cbe6eef-3ebf-320e-a71e-5012956f9036 | -9.78573 | -57.42388 | 2025-06-11 04:49:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b71a764f-0e6a-34b4-a6ef-a46f866d9f37 | -11.77662 | -47.40392 | 2025-06-11 04:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f6bc8a99-c15d-3b6d-99c8-9257be0e2d3e | -11.13793 | -53.91934 | 2025-06-11 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cfe0ee90-62b1-3ce2-88f6-415ab9480424 | -10.70553 | -49.5149 | 2025-06-11 04:49:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2b73865f-cd09-3416-bbb7-065806d7d74d | -8.96579 | -47.96649 | 2025-06-11 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2cfee8fc-6eb2-3aa4-b7a7-b8e9237c3a97 | -11.49675 | -48.58489 | 2025-06-11 04:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 908cdbf9-0438-3c13-bf09-cab0fd63d9dc | -9.47412 | -48.59952 | 2025-06-11 04:49:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abb46217-3c37-3e3b-9e05-eb3ea69f8b71 | -10.51437 | -53.63092 | 2025-06-11 04:49:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7f04f48-c310-3d29-a12e-9f41fddd8d54 | -12.28964 | -52.46913 | 2025-06-11 04:49:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ce17eb5-8ecf-3f13-8f29-5d3330372bc4 | -9.398 | -48.43294 | 2025-06-11 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8b68918-875a-391f-9c78-81792e04ff82 | -9.36316 | -57.43895 | 2025-06-11 04:49:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 133f0ed2-2148-3a4d-afc1-aa50ef7087c8 | -11.57928 | -51.34489 | 2025-06-11 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15de41eb-6dd9-3fd0-bae3-98af2315107f | -11.90484 | -54.82576 | 2025-06-11 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 50a162b8-2e8e-3747-8023-cc5d95993fcf | -9.82393 | -61.40675 | 2025-06-11 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b8ec2d0-794a-3b1d-89e9-bfba9b3d3d6b | -11.38048 | -56.55991 | 2025-06-11 04:49:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebcc45c4-d8a2-3582-a7b7-14b6a50c05f6 | -10.89915 | -42.24556 | 2025-06-11 04:49:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5383be90-25c2-3838-ae9f-650215135d4f | -10.07618 | -52.7513 | 2025-06-11 04:49:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cf5c4e44-be50-37ec-9b6e-b070ab499a6d | -14.50163 | -43.80286 | 2025-06-11 04:49:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5eaafe56-1590-381f-b9f7-26f8f6a9515f | -9.40102 | -48.43779 | 2025-06-11 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 45f6191d-272a-3735-a270-d8d224bfc62c | -14.24545 | -45.49433 | 2025-06-11 04:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27197e01-0158-3719-9ac0-48fe4ad8b8a4 | -10.87996 | -49.55133 | 2025-06-11 04:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ae41f8c-d911-385e-87f5-dbdeec20d66c | -8.9614 | -47.9704 | 2025-06-11 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 831bb891-49de-3bae-a513-b9581c06b5bf | -12.20328 | -54.26454 | 2025-06-11 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a3eafa9-3301-33e3-9efe-0424f2abd51b | -10.24289 | -52.23543 | 2025-06-11 04:49:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1453bba7-d4a8-3bf0-b443-3078d4136078 | -13.09243 | -52.29089 | 2025-06-11 04:49:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e36abad-5034-3a46-a127-cdba98e87f37 | -12.52041 | -57.22327 | 2025-06-11 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| db5ced06-faf8-3d92-b5c0-58b9571e5f1c | -11.82428 | -43.79138 | 2025-06-11 04:49:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dc823ccc-9d33-322e-a56c-57c91ccb239a | -9.60683 | -49.0143 | 2025-06-11 04:49:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e49ae09-155d-3a4a-86e0-41cbfbe2125a | -10.30189 | -57.14129 | 2025-06-11 04:49:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README8.md)
