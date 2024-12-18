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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13407bf7-3141-3af1-a8de-6dbeeb91a6db | -4.24426 | -45.98901 | 2024-12-18 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 50400da9-3cbb-3483-8897-232ec0b31dd0 | -5.94609 | -48.06157 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 67ba4e4a-2931-34cd-bb40-239fc4fe5dc1 | -5.95011 | -48.05842 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dca54391-51d9-3f6b-ad44-3b33e2e17749 | -3.86609 | -47.02914 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 904e89ea-aeba-3efa-9a05-7eccbdda6fb6 | -4.97472 | -43.71916 | 2024-12-18 04:25:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9712c0e0-ddb5-3021-94ec-706f30a90018 | -5.62845 | -44.83529 | 2024-12-18 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e155828-8006-33ee-9e08-6c2165ee35d1 | -6.98615 | -43.5619 | 2024-12-18 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9d6f964d-316a-355d-8e92-65328108c588 | -2.94484 | -41.19778 | 2024-12-18 04:25:00 | NPP-375D | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6717c4ec-0d8c-3ff3-a6f2-bcfa05915409 | -3.69706 | -44.6451 | 2024-12-18 04:25:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 09406ebb-9583-37a6-b07c-a56b9ab6d0b7 | -6.21823 | -46.21801 | 2024-12-18 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 671b65e2-4fc8-3727-833f-5e79ca92935b | -6.98912 | -43.56655 | 2024-12-18 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9561f10-266f-346c-ba2a-9d2ebd68d96e | -5.36148 | -45.20564 | 2024-12-18 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc686708-b87e-3024-ab5a-45ed8f881e86 | -7.19904 | -44.92206 | 2024-12-18 04:25:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5e31512-338e-340a-abe0-2fe2005d1397 | -3.83277 | -46.6865 | 2024-12-18 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 313f4d84-914d-3ce8-b25c-9bb8e8d0a1cc | -3.67818 | -44.7001 | 2024-12-18 04:25:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91f5c34b-5a60-3e33-8f1d-977ef03d4379 | -5.08851 | -45.97653 | 2024-12-18 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1556d8de-932a-323c-8117-b9b3e99d98be | -4.06137 | -46.91425 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd14b54c-8a05-3507-8e0b-ad5f8376502b | -3.8706 | -46.57753 | 2024-12-18 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09f0b62c-4065-3bbf-a101-19432372d24b | -1.70586 | -45.7818 | 2024-12-18 04:25:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c9989279-2c15-3e61-9457-ee1560ebdefb | -1.57388 | -46.03897 | 2024-12-18 04:25:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76f5e4c6-018b-3619-955c-4ad5229e6110 | -5.21629 | -44.904 | 2024-12-18 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47e14915-f6bf-3d48-b7f0-2321b2a54b3e | -3.34043 | -53.02229 | 2024-12-18 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 144e3dce-1dce-351e-8efb-7785aecb2fba | -3.86946 | -47.02967 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 268abdce-2999-3d15-8abd-f046d8d28bba | -4.11195 | -43.22014 | 2024-12-18 04:25:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a00272f6-7b02-344b-89b3-22bad6f0b469 | -3.90964 | -46.66974 | 2024-12-18 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ece92f03-428b-3291-af4c-b0428d5c9187 | -3.24253 | -42.41626 | 2024-12-18 04:25:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 161164fa-6252-3931-9221-ff052483da07 | -5.93882 | -48.06872 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 902ccff3-66d1-3bb5-bc48-b43c7c0a09f4 | -6.05966 | -44.05023 | 2024-12-18 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5b229fa1-b7a4-33ac-ab31-28e2533bb05c | -3.86271 | -47.02861 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 218bd2f4-e6e2-3689-b7ba-32715d79249d | -3.83388 | -46.67952 | 2024-12-18 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 554f9739-bf75-3b05-a454-2fb048823754 | -6.63821 | -47.34264 | 2024-12-18 04:25:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 425a23f7-a7d2-3f5e-a7ed-258ae8e3fae2 | -2.9237 | -45.2477 | 2024-12-18 04:25:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef454715-2a6a-3854-9425-387c52248ad4 | -5.94729 | -48.05419 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8018581c-dbb5-3c3c-8a15-2f1e2ac0e971 | -6.63151 | -47.34156 | 2024-12-18 04:25:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 806124d3-6d73-32de-9575-79b66ce18967 | -4.24372 | -45.99246 | 2024-12-18 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6dadf9f3-5b3e-32cc-b16d-1c670d3076f7 | -3.87228 | -46.58858 | 2024-12-18 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43d32cac-68ef-348e-be0a-ff8e8d3e6f6f | -4.15117 | -43.5673 | 2024-12-18 04:25:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 084daa0b-e4c5-3c85-9536-239b5eeae419 | -2.14227 | -46.46599 | 2024-12-18 04:25:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c766053-fc71-3287-8a6c-d4337bc8fde5 | -6.21768 | -46.22148 | 2024-12-18 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 720db586-6e35-3b25-8dad-cf2bc51dd207 | -4.14828 | -43.56296 | 2024-12-18 04:25:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85e87e31-7335-3816-b9d8-3b69c8d723e5 | -3.85483 | -47.03468 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b953efdc-8826-36fd-bfc3-dcd4b3e1fa1e | -4.30706 | -46.27523 | 2024-12-18 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 064deee6-95f4-3b9f-b88e-40c774dab2b2 | -4.48498 | -42.86811 | 2024-12-18 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2377ac38-071e-3ec4-8671-60da69f8f85b | -3.87507 | -47.03783 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3dfba8a-e47c-3bc9-b9a2-72cbc0b6849a | -3.79749 | -46.84364 | 2024-12-18 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2a587ce-dfcf-3b2d-b285-a3b92ccded7f | -6.19427 | -44.42406 | 2024-12-18 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ff6b82f3-2808-35f7-be0e-7178570ab855 | -2.7032 | -47.73024 | 2024-12-18 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e076e2a-b683-3d1e-baac-4bfedb1204cf | -5.95367 | -39.67688 | 2024-12-18 04:25:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 239831b5-8999-3677-a02d-bc1751866ff0 | -3.87844 | -47.03835 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fbb487c-9129-37b9-9863-f4208e30c737 | -5.57581 | -42.93943 | 2024-12-18 04:25:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2bc97092-4fa8-3611-80dd-5cdb9a6d214f | -6.24964 | -46.91359 | 2024-12-18 04:25:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 69d44dab-05be-3430-b183-a8d85494b144 | -4.67337 | -44.51649 | 2024-12-18 04:25:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c36466f0-3768-3a3a-b187-cad20330f94b | -4.04173 | -47.0167 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5343bf88-c51b-3a5d-bfea-c8c43258c67d | -4.54307 | -43.29372 | 2024-12-18 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 34499fb7-90ef-3044-8be1-65dcc28bf4f3 | -3.84389 | -45.93318 | 2024-12-18 04:25:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0c3fa8f-21e5-32dd-8343-c21b0aedc9d7 | -7.67875 | -46.81905 | 2024-12-18 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5c55fd22-d3e5-32c7-ab66-c6073e56eca7 | -3.91614 | -46.99673 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa1523a1-50a3-3817-9fc8-e9b17fb06f83 | -6.98973 | -43.56245 | 2024-12-18 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 05144f5e-2e84-34fc-8896-74577cf9eaf3 | -1.42622 | -55.45166 | 2024-12-18 04:25:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f974b16c-8156-3054-8cae-10be66abe90d | -3.83332 | -46.68301 | 2024-12-18 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a065f62-4dc8-35c7-b1bb-c18e6789ad94 | -6.98676 | -43.55783 | 2024-12-18 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9ef57dd0-8a8c-35f6-aea1-91d9f3cdb3a8 | -4.01645 | -47.04555 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89d5d2fb-74c7-3200-a722-f479dd76526c | -6.76091 | -40.12951 | 2024-12-18 04:25:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 54b3f5a3-cbdf-3a2b-90c9-2c26b73ea5cd | -5.39684 | -46.57498 | 2024-12-18 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee2e123b-7cdd-3a15-9f3a-c643a51e699a | -2.69647 | -46.60316 | 2024-12-18 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1354b2bb-1844-331a-837e-cfe2614d8390 | -3.85426 | -47.03824 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 642e74e3-de8d-360e-8202-870909b852ab | -4.24568 | -46.9865 | 2024-12-18 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ada72b9-02b5-3d76-80a7-976f8631f410 | -5.94488 | -48.06902 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1215bd32-50d1-3c7b-ab53-f124fb084a27 | -6.28409 | -39.58465 | 2024-12-18 04:25:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8c12952b-744f-3c93-8285-8387a5545c59 | -3.02305 | -45.23825 | 2024-12-18 04:25:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13f8f112-af5c-3db4-8ea7-bdcb1c5780ea | -6.30594 | -38.90883 | 2024-12-18 04:25:00 | NPP-375D | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0cef260d-6304-373d-bcc7-73efeb8dcc32 | -5.94626 | -48.0661 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47702a93-a189-3537-97df-aa822b699432 | -4.67281 | -44.5201 | 2024-12-18 04:25:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8b21616-4d72-3e9e-bcbd-de5b0aa3b820 | -1.52046 | -46.0521 | 2024-12-18 04:25:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a5a1b92-c22e-3f59-8aee-e2a88b732323 | -4.16507 | -43.96933 | 2024-12-18 04:25:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4565b48e-0051-3392-9756-5ac17068d22a | -4.48719 | -42.86993 | 2024-12-18 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a91b92a-5823-39fc-94de-43d8eb316be8 | -5.234 | -45.48388 | 2024-12-18 04:25:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6be25f6-d6c1-35f4-bb8d-75a5f239fd30 | -7.86374 | -43.08992 | 2024-12-18 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 31942e36-d0f4-3098-8dac-575d14d8de84 | -5.40072 | -46.57203 | 2024-12-18 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f63efeb6-df4f-3e07-b09c-9c77bd6b8364 | -2.79739 | -47.4256 | 2024-12-18 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8c8571b8-bcc4-330d-88cd-bdd0b0d21455 | -5.11286 | -43.31469 | 2024-12-18 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 701a8f10-46f4-35e1-809b-caba4ee32e08 | -2.23827 | -53.74245 | 2024-12-18 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8e2a0b99-0ad5-3848-8fce-bf692ef6b5e0 | -6.20826 | -46.21645 | 2024-12-18 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10d10450-082c-397c-b516-78617c7dfcaa | -4.03781 | -47.0197 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d49e99e2-164e-329e-8825-847071d102ca | -3.14626 | -44.4556 | 2024-12-18 04:25:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4ab1222-ddf7-36a7-b434-bb66fed161b4 | -4.11981 | -43.56253 | 2024-12-18 04:25:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26e57d4e-b30b-39c6-96aa-1bccfeee64cc | -2.25533 | -45.59927 | 2024-12-18 04:25:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9275ee10-a5da-346c-aa09-249fa2a4968f | -4.97182 | -43.71479 | 2024-12-18 04:25:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c380362c-c4e2-320f-bf87-6b17211df1fd | -5.73129 | -39.53835 | 2024-12-18 04:25:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7d15aa69-81e9-361a-b8ed-7208e506ae82 | -6.19189 | -44.4204 | 2024-12-18 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27afe0c0-9640-32cf-85a0-f66486f6ab34 | -3.87003 | -47.0261 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94ac4bb9-a8a7-367a-ad13-d8ef3410b417 | -6.43729 | -40.62282 | 2024-12-18 04:25:00 | NPP-375D | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| ee51d2d3-aa6f-3cd8-882f-afacbbf73151 | -2.40676 | -47.7084 | 2024-12-18 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23c50e4f-2b40-30eb-bf63-420878a6afd8 | -4.0451 | -47.01726 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e290fd5-9f11-312c-acc8-05328e9494b0 | -3.86666 | -47.02557 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d3650b7d-7513-3448-bc97-159f069365ac | -7.81224 | -46.20834 | 2024-12-18 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd6f15da-5e6a-352a-a2ef-0eab5c54ded0 | -1.6224 | -45.86111 | 2024-12-18 04:25:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28ed632a-a4c8-368c-8c93-e250c745a615 | -5.80796 | -43.05296 | 2024-12-18 04:25:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 345c016e-8fcc-3687-8c99-59b97ee72142 | -3.86215 | -47.03217 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e821263-afc4-3cfd-ace8-29a8544d9c6d | -4.03499 | -47.03754 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README15.md)
